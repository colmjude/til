#!/usr/bin/env python3

import os
import jinja2
from config import Config
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from note import Notes, Note, note_index
from helpers import file_mod_timestamp, timestamp_datetime, slugify


config = Config()


def file_slug(filename: str):
    return filename.split("/")[-1].replace(".md", "")


def initiate_markdown():
    idx = note_index()

    def wikilink_builder(label, base, end):
        # this only does top level notes
        # e.g. /notes/<note slug>.html
        # need to do something more comprehensive
        # notes = Notes(config.NOTES_ROOT)
        # url = f"{base}{title_to_slug(label)}{end}"
        return idx.get(label) + end

    return markdown.Markdown(
        extensions=[
            "meta",
            WikiLinkExtension(
                base_url="/notes/", end_url=".html", build_url=wikilink_builder
            ),
        ]
    )


def render(path, template, **kwargs):
    # path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(**kwargs))


loader = jinja2.FileSystemLoader(searchpath="./templates")
env = jinja2.Environment(loader=loader)
note_template = env.get_template("note.html")
list_template = env.get_template("list.html")
tags_template = env.get_template("tags.html")


notes = Notes(config.NOTES_ROOT, initiate_markdown())
notes_list = []


def create_missing_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


for note in notes.notes.values():
    if not note.draft:
        notes_list.append(note.get_json())
        n = note.path.replace(note.filename, note.slug)
        n = n.replace(config.NOTES_ROOT, config.DIST_ROOT)
        create_missing_dir(n)
        render(
            f"{n}/index.html",
            note_template,
            markdown_output=note.get_html(),
            frontmatter=note.get_frontmatter(),
        )
        print(f"Created {n}/index.html")

# want it in chronilogical order
sorted_notes = sorted(
    notes_list, key=lambda n: n["frontmatter"]["mod_timestamp"], reverse=True
)
render(config.DIST_ROOT + "index.html", list_template, notes=sorted_notes)

tags = {}
for n in notes_list:
    for tag in n["frontmatter"]["tags"]:
        tags.setdefault(tag, {"notes": []})
        tags[tag]["notes"].append(n)

for tag in tags.keys():
    render(
        config.DIST_ROOT + "tag/" + slugify(tag) + "/index.html",
        list_template,
        notes=tags[tag]["notes"],
        list_title=f"Tag: {tag}",
    )

# render list of tags page
sorted_tags = dict(sorted(tags.items(), key=lambda item: item[0]))
render(config.DIST_ROOT + "tag/index.html", tags_template, tags=sorted_tags)
