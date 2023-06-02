---
title: "If-else statements in Make"
tags: development, make
author: Colm Britton
created: 2021/10/12
updated: 2021/10/12
---

You can use `if/else` statements in your makefiles.

A good use case is to check a dependency is installed and available. It is an opportunity to warn the user about what is missing.

For example, the following checks `datasette` is available before executing the datasette command.

```
server:
ifeq (,$(shell which datasette))
    $(error datasette does not exist!)
endif
	datasette -m metadata.json view_model.db
```
