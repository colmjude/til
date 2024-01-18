---
title: "Flake8"
tags: webdev, python, commandline, development
author: Colm Britton
created: 2022/01/29
updated: 2024/01/18
---

The Digital Land team use [flake8](https://flake8.pycqa.org/en/latest/) (style guide enforcement).

They used a `setup.cfg`, in the root dir of your project, for the rules flake8 for follow. E.g.

    [flake8]
    max-line-length = 180
    ignore = E203, W503


### Exclude files

[Exlude files](https://flake8.pycqa.org/en/latest/user/options.html?highlight=exclude#cmdoption-flake8-exclude) using the `--exclude` option. It accepts a comma-separated list of patterns to ignore. E.g.

    flake8 --exclude==.venv,node_modules .

### Config file for python projects

I have created a [gist](https://gist.github.com/colmjude/7cd1a57609a636b3cd2fb65bd5ece182) so that I can use a similar setup for all python projects.

### Using with visual studio code

My preferred approach is to use a `.flake8` file to configure flake8. Example contents is:

```
[flake8]
max-line-length = 120
; W291 	Trailing whitespace
; E203 	Whitespace before ':'
; W503 	Line break occurred before a binary operator
; W391  Blank line at end of file
ignore = W291, E203, W503, W391
exclude =
    __pycache__
    node_modules
		.venv
		migrations

; vim: ft=dosini
```

To using it with visual studio code you now need to install a specific extension ([flake8 extension]()https://marketplace.visualstudio.com/items?itemName=ms-python.flake8).

Then in `settings.json` add the following line to point the extension at your config file.

```
"flake8.args": ["--config", "${workspaceFolder}/.flake8"],
```
