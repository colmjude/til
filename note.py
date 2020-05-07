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

    def get_frontmatter(self):
        f = self.frontmatter
        if 'title' in self.frontmatter.keys():
            f['title'] = self.frontmatter['title'][0]
        return f

    def get_mod_date(self, readable=False):
        if readable:
            return timestamp_datetime(self.mod_date)
        return self.mod_date