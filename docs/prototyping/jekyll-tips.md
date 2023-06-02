---
title: Jekyll tips
tags: prototyping, development, jekyll, github-pages
author: Colm Britton
created: 2022/10/28
updated: 2022/11/01
---

Can extend a template by adding frontmatter to `.html` template file. E.g. extend `default.html` with

```
---
layout: default
---

<!-- html content -->
```

Include content from other files with `include_relative`. [Jekyll docs on include_relative](https://jekyllrb.com/docs/includes/#including-files-relative-to-another-file)

```
{% include_relative _members/team-member-1.md %}
```

Only works for files in or below current directory.

You can add classes to rendered markdown blocks. And other attributes too but the main use case is for css classes.

```
> a blockquote with an added class
{: .css-class}
```

GitHub pages uses [Kramdown markdown](https://kramdown.gettalong.org/).
You can achieve the same effect in python by enabling the [attr_list](https://python-markdown.github.io/extensions/attr_list/) extension. E.g. `markdown.markdown(some_text, extensions=['attr_list'])`.

You can set [Front matter defaults](https://jekyllrb.com/docs/configuration/front-matter-defaults/). You do this in `config.yml`.

For example, if you want to set an attribute on all posts you can put

```
defaults:
  -
    scope:
      path: ""      # empty string for all files
      type: posts   # limit to posts
    values:
      is_post: true # automatically set is_post=true for all posts
```
