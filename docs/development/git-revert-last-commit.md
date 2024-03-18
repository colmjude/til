---
title: "Git, revert last commit"
tags: webdev, git, commandline
author: Colm Britton
created: 2022/08/31
updated: 2023/09/11
---

Sometimes I make a commit accidentally or make a mistake; miss a file, add a file I shouldn't, leave a debug (print statement), etc.

I need to fix the mistake, and pretend it never happened in the first place. So I need to revert the last commit.

I do it with:

    git reset HEAD~
    .
    // do your stuff
    git add <your files>
    git commit -c ORIG_HEAD

The `git commit -c ORIG_HEAD` command will open the editor with previous commit message. Edit away.

Apparently, using `-C` argument means you don't need to change the commit message.

#### Delete last commit

Alternatively, you can remove the commit completely.

To do so add the `--hard` option to the previous `reset` command.

    git reset --hard HEAD~1

Remember this is a destructive command, it will delete the last commit and any currently uncommitted changes. If you want to keep them `stash` them before running the previous command.
