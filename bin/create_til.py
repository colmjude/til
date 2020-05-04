#!/usr/bin/env python3

import os
import sys

frontmatter_str = """
title: "<<title>>"
tags:
author: Colm Britton
--------------------

"""


til_dir = "docs/"


def title_to_filename(title):
    return title.lower().replace(" ", "-")


def create_file(title):
    til_file = open(os.path.join(til_dir, f"{title_to_filename(title)}.md"), 'w')
    til_file.write(frontmatter_str.replace("<<title>>", title))
    til_file.close()


if __name__ == "__main__":
    if len(sys.argv[1:]):
        create_file(sys.argv[1])
    else:
        print("No title provided")