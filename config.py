# -*- coding: utf-8 -*-
import json
import os

from dotenv import load_dotenv
load_dotenv()

class Config(object):
    NOTES_ROOT = "docs/"
    DIST_ROOT = "dist/notes/"

