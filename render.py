#!/usr/bin/env python3

import os
import jinja2
from config import Config

from note import Note
from helpers import file_mod_timestamp, timestamp_datetime


config = Config()


def file_slug(filename: str):
    return filename.split("/")[-1].replace(".md", "")


def collect_notes():
    dnames = []
    fnames = []
    for root, dir_names, file_names in os.walk(config.NOTES_ROOT):
        for d in dir_names:
            dnames.append(os.path.join(root, d))
        for f in file_names:
            fnames.append(os.path.join(root, f))
    return dnames, fnames


def render(path, template, **kwargs):
    #path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(**kwargs))


loader = jinja2.FileSystemLoader(searchpath="./templates")
env = jinja2.Environment(loader=loader)
note_template = env.get_template("note.html")
list_template = env.get_template("list.html")

dirs, files = collect_notes()

notes = []

for f in files:
    note = Note(f)
    notes.append(note.get_json())
    f = f.replace(config.NOTES_ROOT, config.DIST_ROOT)
    f = f.replace(".md", "")
    render(f + ".html", note_template, markdown_output=note.get_html(), frontmatter=note.get_frontmatter())
    print(f"Created {f}")

# want it in chronilogical order
sorted_notes = sorted(notes, key=lambda n: n['frontmatter']['mod_date'], reverse=True)
render(config.DIST_ROOT + "index.html", list_template, notes=sorted_notes)

