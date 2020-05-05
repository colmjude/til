#!/usr/bin/env python3

import os
import jinja2

from note import Note
from helpers import file_mod_timestamp, timestamp_datetime

dist_dir = "dist/notes/"

note = Note("docs/hide-from-users.md")


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

render(dist_dir + "/index.html", note_template, markdown_output=note.get_html())

