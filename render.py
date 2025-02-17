#!/usr/bin/env python3

import os
import re
import jinja2
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from config import Config
from helpers import file_mod_timestamp, slugify, timestamp_datetime
from note import Note, Notes, note_index
from application.jinja_setup import setup_jinja
from markdowntweetembed.tweetembed import TweetEmbedExtension

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

    # use getattr because config is an object with attributes not a dict
    tw_config = getattr(config, "TW_CONFIG")
    return markdown.Markdown(
        extensions=[
            "meta",
            WikiLinkExtension(
                base_url="/notes/", end_url=".html", build_url=wikilink_builder
            ),
            "fenced_code",
            TweetEmbedExtension(**tw_config),
        ]
    )


def render(path, template, **kwargs):
    # path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        f.write(template.render(**kwargs))


env = setup_jinja()

note_template = env.get_template("note.html")
list_template = env.get_template("list.html")
tags_template = env.get_template("tags.html")


notes = Notes(config.NOTES_ROOT, initiate_markdown())
notes_list = []


def create_missing_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


def strip_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix) :]
    return s


for note in notes.notes.values():
    if not note.draft:
        notes_list.append(note.get_json())
        n = note.path.replace(note.filename, note.slug)
        n = n.replace(config.NOTES_ROOT, config.DIST_ROOT)
        canonical_path = strip_prefix(
            note.path.replace(note.filename, note.slug), "docs/"
        )
        create_missing_dir(n)
        render(
            f"{n}/index.html",
            note_template,
            markdown_output=note.get_html(),
            frontmatter=note.get_frontmatter(),
            canonical_url="{}/{}/".format(config.BASE_URL, canonical_path),
            note=note,
            edit_url="{}/{}".format(config.REPO_BASE_URL, note.path),
        )
        print(f"Created {n}/index.html")

# want it in chronilogical order
sorted_notes = sorted(
    notes_list, key=lambda n: n["frontmatter"]["updated_timestamp"], reverse=True
)
render(
    config.DIST_ROOT + "index.html",
    list_template,
    notes=sorted_notes,
    notes_page_classes="notes-index-page",
)

tags = {}
for n in notes_list:
    for tag in n["frontmatter"]["tags"]:
        tags.setdefault(tag, {"notes": []})
        tags[tag]["notes"].append(n)


def extract_weeknote_number(title):
    match = re.search(r"\d+", title)
    return int(match.group()) if match else 0


for tag in tags.keys():
    if tag == "weeknote":
        weeknotes = sorted(
            tags[tag]["notes"],
            key=lambda n: extract_weeknote_number(n["frontmatter"]["title"]),
            reverse=True,
        )
        render(
            config.DIST_ROOT + "weeknote/index.html",
            list_template,
            notes=weeknotes,
            list_title="Weeknotes",
            notes_page_classes="notes-weeknote-page",
            tag=tag,
        )
    else:
        render(
            config.DIST_ROOT + "tag/" + slugify(tag) + "/index.html",
            list_template,
            notes=tags[tag]["notes"],
            list_title=f"Tag: {tag}",
            notes_page_classes="notes-tag-page",
            tag=tag,
        )

# render list of tags page
sorted_tags = dict(sorted(tags.items(), key=lambda item: item[0]))
render(config.DIST_ROOT + "tag/index.html", tags_template, tags=sorted_tags)
