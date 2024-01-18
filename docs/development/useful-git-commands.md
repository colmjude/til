---
title: "Useful Git commands"
tags: development, commandline, git, tips, clean
author: Colm Britton
created: 2023/01/16
updated: 2024/01/18
---

Git commands I find useful.

Remove files from git without deleting them (aka keep a local copy)

```
git rm --cached <file>
```

Add `-r` flag removing a `<folder>`.

### Remove untracked filed

Use this command

```
git clean -f -d
```
`-f` forces it to remove untracked files
`-d` will make it remove the untracked directories
