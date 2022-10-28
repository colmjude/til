title: Jekyll tips
tags: prototyping, development, jekyll, github-pages
author: Colm Britton
created: 2022/10/28
updated: 2022/10/28
--------------------

Can extend a template by adding frontmatter to `.html` template file. E.g. extend `default.html` with

```
---
layout: default
---

<!-- html content -->
```

Include content from other files with `include_relative`.

```
{% include_relative _members/team-member-1.md %}
```

Only works for files in or below current directory.
