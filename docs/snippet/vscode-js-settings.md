title: JS settings for VSCode
tags: webdev, development, snippet, productivity, vscode
author: Colm Britton
--------------------

I follow the StandardJs guidelines for any JS I write.

You can set up vscode to apply StandardJS formatting on save.

First, install the [StandardJS extension](https://marketplace.visualstudio.com/items?itemName=standard.vscode-standard). You also need to install `standard` package, to do so list it in the project's `package.json` file.

Add the lines to the `.vscode/settings.json` file.


    // Prevents VS Code from formatting JavaScript with the default linter
    "javascript.format.enable": false,
    // Prevents VS Code linting JavaScript with the default linter
    "javascript.validate.enable": false,
    // Lints with Standard JS
    "standard.enable": true,
    // Format files with Standard whenever you save the file
    "standard.autoFixOnSave": true,
    // Files to validate with Standard JS
    "standard.validate": [
        "javascript",
        "javascriptreact"
    ]
