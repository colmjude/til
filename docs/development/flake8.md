title: "Flake8"
tags: webdev, python, commandline, development
author: Colm Britton
--------------------

The Digital Land team use [flake8](https://flake8.pycqa.org/en/latest/)(style guide enforcement).

`setup.cfg`, in the root dir of your project, contains configuration rules for flake8. E.g.

    [flake8]
    max-line-length = 180
    ignore = E203, W503


### Exclude files

[Exlude files](https://flake8.pycqa.org/en/latest/user/options.html?highlight=exclude#cmdoption-flake8-exclude) using the `--exclude` option. It accepts a comma-separated list of patterns to ignore. E.g.

    flake8 --exclude==.venv,node_modules .
