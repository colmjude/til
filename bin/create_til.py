#!/usr/bin/env python3

import os
import sys
import datetime

frontmatter_str = """title: "<<title>>"
tags:
author: Colm Britton
created: <<date>>
draft: True
--------------------
"""


base_dir = "docs/"


def title_to_filename(title):
    return title.lower().replace(" ", "-")


def replace_frontmatter_placeholder(text, placeholder, val):
    return text.replace(placeholder, val)


def prepare_template(title):
    today = datetime.date.today().strftime("%Y/%m/%d")
    frontmatter = replace_frontmatter_placeholder(frontmatter_str, "<<title>>", title)
    frontmatter = replace_frontmatter_placeholder(frontmatter, "<<date>>", today)
    return frontmatter


def save_markdown_file(path, content):
    til_file = open(path, 'w')
    til_file.write(content)
    til_file.close()


def create_file(args):
    til_dir = base_dir

    if len(args) > 1:
        til_dir = til_dir + args[1]

    if not os.path.isdir(til_dir):
        os.mkdir(til_dir)

    til_path = os.path.join(til_dir, f"{title_to_filename(args[0])}.md")
    if os.path.isfile(til_path):
        print(f"ERROR: {til_path} already exists")
    else:
        content = prepare_template(args[0])
        save_markdown_file(til_path, content)


if __name__ == "__main__":
    args_provided = sys.argv[1:]
    if len(args_provided):
        create_file(args_provided)
    else:
        print("No title provided")