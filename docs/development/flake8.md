
title: "Flake8"
tags: webdev, python, commandline, development
author: Colm Britton
--------------------

The Digital Land team use flake8 to ...

### Exclude files

[Exlude files](https://flake8.pycqa.org/en/latest/user/options.html?highlight=exclude#cmdoption-flake8-exclude) using the `--exclude` option. It accepts a comma-separated list of patterns to ignore. E.g.

    flake8 --exclude==.venv,node_modules .
