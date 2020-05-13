#!/usr/bin/env python3

import os
import sys

frontmatter_str = """title: "<<title>>"
tags:
author: Colm Britton
--------------------

"""


base_dir = "docs/"


def title_to_filename(title):
    return title.lower().replace(" ", "-")


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
        til_file = open(til_path, 'w')
        til_file.write(frontmatter_str.replace("<<title>>", args[0]))
        til_file.close()


if __name__ == "__main__":
    args_provided = sys.argv[1:]
    if len(args_provided):
        create_file(args_provided)
    else:
        print("No title provided")