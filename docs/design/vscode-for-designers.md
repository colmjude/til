---
title: VSCode for designers
tags: webdev, design, vscode, css
author: Colm Britton
created: 2024/07/03
updated: 2024/07/03
---

As a designer I often jump into vscode to work on designs, components and pages.

To help I've started configuring vscode to work for me, and maybe other designers too. Here are a few of my favourite extensions and how I use them.

### Speeding up and checking classes

I've recently moved on from SCSS Everywhere to [HTML CSS Support](https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css).

This extension makes it easier to use the classes you want to use. You can use your css classes and any css classes of stylesheets you include in your projects.

Set it up by telling it where to find the stylesheets. And, if you want to validate the classes on save of .html files add that option too. Validate just checks the classes you have used exist in your stylesheets somewhere.

For example, add the following to `settings.json`
```
{
  "css.styleSheets": ["docs/static/**/*.css"],
  "css.autoValidation": "Save",
}
``
