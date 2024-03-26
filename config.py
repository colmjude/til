# -*- coding: utf-8 -*-
import datetime
import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    NOTES_ROOT = "docs/"
    DIST_ROOT = "dist/notes/"
    CURRENT_YEAR = datetime.date.today().year
    BASE_URL = "https://colmjude.com/notes"
    REPO_BASE_URL = "https://github.com/colmjude/til/edit/main/"
    TW_CONFIG = {
        "TW_API_KEY": os.getenv("TW_API_KEY"),
        "TW_API_KEY_SECRET": os.getenv("TW_API_KEY_SECRET"),
        "TW_ACCESS_TOKEN": os.getenv("TW_ACCESS_TOKEN"),
        "TW_ACCESS_TOKEN_SECRET": os.getenv("TW_ACCESS_TOKEN_SECRET"),
    }
