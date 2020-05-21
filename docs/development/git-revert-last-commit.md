title: "Git, revert last commit"
tags: webdev, git, commandline
author: Colm Britton
--------------------

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
