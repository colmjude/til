#!/usr/bin/env python3

import os
import codecs
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from helpers import file_mod_timestamp, timestamp_datetime, title_to_slug


def wikilink_builder(label, base, end):
    # this only does top level notes
    # e.g. /notes/<note slug>.html
    # need to do something more comprehensive
    url = f"{base}{title_to_slug(label)}{end}"
    return url


md = markdown.Markdown(extensions = ['meta', WikiLinkExtension(base_url='/notes/', end_url='.html', build_url=wikilink_builder)])

class Note:
    def __init__(self, path):
        self.path = path
        self.read_file()
        self.date_format = '%d %B %Y'
        self.slug = self.make_slug()

    def make_slug(self):
        path = self.path
        original_name = path.split("/")[-1]
        slug = self.path.split("/")[-1].replace(".md", "")
        return path.replace(original_name, slug.replace(".", "-"))

    def read_file(self):
        _file = codecs.open(self.path, mode="r")
        self.raw_contents = _file.read()
        self.note = md.convert(self.raw_contents)
        self.frontmatter = md.Meta
        self.draft = self.is_draft()
        self.mod_date = file_mod_timestamp(self.path)

    def is_draft(self):
        fm_draft = self.frontmatter.get('draft')
        if fm_draft is not None:
            if fm_draft[0].lower() == 'true':
                return True
        return False

    def get_html(self):
        return self.note

    def get_raw(self):
        return self.raw

    def extract_title(self):
        title = ''
        if 'title' in self.frontmatter.keys():
            titles = self.frontmatter.get('title')
            return titles[0].strip('\"')

    # converts ['frontend, js']
    # to ['frontend', 'js']
    def extract_tags(self):
        return [t.strip(" ").lower() for t in self.frontmatter['tags'][0].split(",")]

    def get_frontmatter(self):
        # make a copy
        f = dict(self.frontmatter)
        
        f['title'] = self.extract_title()
        f['tags'] = self.extract_tags()
        f['mod_date'] = self.get_mod_date(True)
        f['mod_timestamp'] = self.get_mod_date()
        
        if 'heroclasses' in f.keys():
            class_list = self.extract_as_list(f['heroclasses'][0], ',')
            f['heroclasses'] = " ".join(class_list)

        return f

    def get_mod_date(self, readable=False):
        if readable:
            return timestamp_datetime(self.mod_date, format=self.date_format)
        return self.mod_date

    def get_url(self):
        d = os.path.dirname(self.path)
        d = d.replace("docs", "notes", 1)
        return "/" + d + "/" + self.slug

    def extract_as_list(self, str, splitter):
        return str.split(splitter)

    def get_json(self):
        return {
            'html': self.get_html(),
            'frontmatter': self.get_frontmatter(),
            'url': self.get_url()
        }
