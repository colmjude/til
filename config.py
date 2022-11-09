# -*- coding: utf-8 -*-
import json
import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    NOTES_ROOT = "docs/"
    DIST_ROOT = "dist/notes/"
    BASE_URL = "https://colmjude.com/notes"
    REPO_BASE_URL = "https://github.com/colmjude/til/edit/main/"
