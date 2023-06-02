---
title: Python settings for VSCode
tags: webdev, development, snippet, productivity, vscode
author: Colm Britton
---

I've been using Visual studio code since early 2020. I have been able to write more and better Python code by using a few of the inbuilt python features.

To get the most out of VSCode when workon on Python code you need to set a few settings for the project (workspace in VSCode).

Here are the most common things I set. These go in the `.vscode/settings.json` file.


    {
        "python.pythonPath": "/Users/Colm/.virtualenvs/dlf/bin/python",
        "python.formatting.provider": "black",
        "[python]": {
            "editor.formatOnSave": true
        },
        "python.testing.pytestEnabled": true,
        "python.testing.pytestPath": "/Users/Colm/.virtualenvs/dlf/bin/pytest"
    }


`python.pythonPath` is the path to python executable(?) in the virtualenv for the project. You can set this manually or hit `shift+command+p`, select `Python: Select Interpreter` and choose the right virtualenv.

`python.formatting.provider` is the formatter of your choice. The Digital Land Team use `black` which is great, it cleans up your code to match an opinionated style. It is handy. It needs to be installed, you can do that with `pip install black`.

`editor.formatOnSave`, if set to true, will perform the formatting whenever you save the file. Put it in a `[python]` object if you only want to format python documents on save.

`python.testing.pytestEnabled`, if set to true, activates VSCode's pytest features.

`python.testing.pytestPath` allows you to provide a path to a pytest version/install. You should set this to the pytest in the project's virtualenv otherwise the tests won't have access to all the packages needed. I don't know why you need to set this separately but without it the tests returned an error. I found [the solution on stackoverflow](https://stackoverflow.com/questions/64589254/vscode-does-not-run-pytest-properly-from-virtual-environment).
