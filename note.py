#!/usr/bin/env python3

import codecs
import os
from datetime import datetime

import frontmatter

import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from config import Config
from helpers import file_mod_timestamp, timestamp_datetime

config = Config()


def note_index():
    md_list = markdown.Markdown(extensions=["meta", "fenced_code"])
    notes = Notes(config.NOTES_ROOT, md_list)
    idx = {k: v.get_url() for k, v in notes.notes.items()}
    return idx


class Notes:
    def __init__(self, root_dir, md):
        self.root_dir = root_dir
        self.md = md
        self.notes = self.collect()

    def collect(self):
        dnames = []
        fnames = []
        for root, dir_names, file_names in os.walk(self.root_dir):
            for d in dir_names:
                dnames.append(os.path.join(root, d))
            for f in file_names:
                fnames.append(os.path.join(root, f))
        notes = {}
        for f in fnames:
            note = Note(f, self.md)
            notes.setdefault(note.title, note)
        return notes

    def get_note(self, title):
        return self.notes.get(title)


class Note:
    def __init__(self, path, md):
        print(path)
        self.path = path
        self.dir = "/".join(path.split("/")[:-1])
        self.parent_category = ""
        if "/" in self.dir:
            self.parent_category = self.dir.split("/")[-1]
        self.filename = path.split("/")[-1]
        self.md = md

        self.read_file()
        self.date_format = "%d %B %Y"
        self.slug = self.make_slug()

    def split_filename(self):
        path = self.path
        if "/" in path:
            self.dir = "/".join(path.split("/")[:-1])
            self.filename = path.split("/")[-1]
        else:
            print(self.path)
            self.dir = "/"
            self.filename = path

    def make_slug(self):
        parts = self.filename.split(".md")
        filename = parts[0].replace(" ", "-")
        return filename.replace(".", "-")

    def extract_frontmatter(self):
        _note = frontmatter.load(self.path)
        return _note.metadata

    def read_file(self):
        _file = codecs.open(self.path, mode="r")
        self.raw_contents = _file.read()
        self.note = self.md.convert(self.raw_contents)
        self.markdown_content = "\n".join(self.md.lines)
        self.frontmatter = self.extract_frontmatter()
        self.draft = self.is_draft()
        self.mod_date = file_mod_timestamp(self.path)
        self.title = self.extract_title()
        created_date = self.frontmatter.get("created", "2000/01/01")
        self.created_date = (
            datetime.strptime(created_date, "%Y/%m/%d").timestamp()
            if self.frontmatter.get("created")
            else file_mod_timestamp(self.path)
        )
        self.updated_date = (
            datetime.strptime(
                self.frontmatter.get("updated", created_date), "%Y/%m/%d"
            ).timestamp()
            if self.frontmatter.get("updated")
            else file_mod_timestamp(self.path)
        )

    def is_draft(self):
        fm_draft = self.frontmatter.get("draft", False)
        if fm_draft:
            return True
        return False

    def get_html(self):
        return self.note

    def get_raw(self):
        return self.raw

    def extract_title(self):
        return self.frontmatter.get("title").strip('"')

    # converts ['frontend, js']
    # to ['frontend', 'js']
    def extract_tags(self):
        tags = self.frontmatter.get("tags", "")
        if tags:
            return [t.strip(" ").lower() for t in tags.split(",")]
        return []

    def get_frontmatter(self):
        # make a copy
        f = dict(self.frontmatter)

        f["title"] = self.extract_title()
        f["description"] = (
            self.frontmatter.get("description")[0].strip('"')
            if self.frontmatter.get("description")
            else None
        )
        f["tags"] = self.extract_tags()
        # not sure this works so going to use updated date if it exists
        f["mod_date"] = timestamp_datetime(self.mod_date, format=self.date_format)
        f["mod_timestamp"] = self.mod_date

        f["created_date"] = timestamp_datetime(
            self.created_date, format=self.date_format
        )
        f["created_timestamp"] = self.created_date
        f["updated_date"] = timestamp_datetime(
            self.updated_date, format=self.date_format
        )
        f["updated_timestamp"] = self.updated_date

        if "heroclasses" in f.keys():
            class_list = self.extract_as_list(f["heroclasses"][0], ",")
            f["heroclasses"] = " ".join(class_list)

        return f

    def get_url(self):
        d = os.path.dirname(self.path)
        # improve this
        d = d.replace("docs", "notes", 1)
        return "/" + d + "/" + self.slug

    def extract_as_list(self, str, splitter):
        return str.split(splitter)

    def get_json(self):
        return {
            "html": self.get_html(),
            "frontmatter": self.get_frontmatter(),
            "url": self.get_url(),
        }

    def to_json(self):
        return {
            "content": self.markdown_content,
            **self.get_frontmatter(),
            "section": self.parent_category,
            "slug": self.slug,
            "url": self.get_url(),
        }
