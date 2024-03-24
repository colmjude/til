#!/usr/bin/env python3

import os
from datetime import datetime


def timestamp_datetime(timestamp, format="%Y-%m-%d %H:%M"):
    return datetime.fromtimestamp(timestamp).strftime(format)


def file_mod_timestamp(path):
    return os.path.getmtime(path)


def file_slug(filename: str):
    return filename.split("/")[-1].replace(".md", "")


def slugify(s):
    return s.lower().replace(" ", "-")
