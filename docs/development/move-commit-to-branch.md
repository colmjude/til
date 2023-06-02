---
title: "Move a commit to a different branch"
tags: webdev, git, commandline
author: Colm Britton
---

Sometimes you might be working on a branch. Maybe it is a new feature or an experiment. But a change you make should apply across the board straight away. Not only when the feature is complete.

Use the `cherry-pick` feature.

Firstly, commit the change to the branch you are working in.

Make a note of the commit hash - `git log`.

Then `checkout` the branch you want to move it to. E.g. `git checkout main`.

Use the `cherry-pick` command to move the commit.

    git cherry-pick <commit-hash>

At this point the commit is on the `main` branch.

You can correct the history on the WIP branch by running:

    git checkout <wip-branch>
    git rebase main

This works for me but if anyone thinks this can or should be done differently, do let me know.
