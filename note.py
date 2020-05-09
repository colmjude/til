#!/usr/bin/env python3

import os
import codecs
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from helpers import file_mod_timestamp, timestamp_datetime

md = markdown.Markdown(extensions = ['meta', WikiLinkExtension(base_url='/notes/', end_url='.html')])

class Note:
    def __init__(self, path):
        self.path = path
        self.read_file()
        self.date_format = '%d %B %Y'
        self.slug = path.split("/")[-1].replace(".md", "")

    def read_file(self):
        _file = codecs.open(self.path, mode="r")
        self.raw_contents = _file.read()
        self.note = md.convert(self.raw_contents)
        self.frontmatter = md.Meta
        self.mod_date = file_mod_timestamp(self.path)

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
        return f

    def get_mod_date(self, readable=False):
        if readable:
            return timestamp_datetime(self.mod_date, format=self.date_format)
        return self.mod_date

    def get_url(self):
        d = os.path.dirname(self.path)
        d = d.replace("docs", "notes", 1)
        return "/" + d + "/" + self.slug

    def get_json(self):
        return {
            'html': self.get_html(),
            'frontmatter': self.get_frontmatter(),
            'url': self.get_url()
        }
