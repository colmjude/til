---
title: "Useful Git commands"
tags: development, commandline, git, tips, clean
author: Colm Britton
created: 2023/01/16
updated: 2024/03/21
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

### Reset changed files

Sometimes files have changed but you don't want to commit the changes. These changed files might also stop you pulling the latest changes from github. In this case you want to remove or reset the changes.

One way to do it is by checking out the file. This will checkout the version from the last commit. 

```
# this will reset a single file
git checkout <file>

# this will reset a whole directory
git checkout <dir>
```

I've set up an alias so I use

```
git co <dir/file>
```
