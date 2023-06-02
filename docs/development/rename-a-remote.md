---
title: Rename a remote
tags: git, development
author: Colm Britton
created: 2022/10/12
updated: 2022/10/12
description: How to change url of a git remote
---

If you need to change the url of a remote use the `git remote set-url` command. For example,

```
git remote set-url origin <url-to-git-repository>
```

You can then check it has changed by running

```
git remote -v
```

This will output the remotes for the repository.
