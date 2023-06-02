---
title: Change an old commit
tags: webdev, git, commandline, development
author: Colm Britton
created: 2023/01/23
updated: 2023/01/23
---

Sometimes you might need to change an old commit. For example, I recently noticed I'd included an api in a commit. I don;t want people seeing that so deleting it in a new commit isn't enough. It would still be in the commit hostory if I did that so I needed a way to remove as if it had never been there.

I've written [a note about amending the last commit](/notes/development/git-revert-last-commit/). These steps are for changing a commit that is older than that.

You need the commit id, for example `199c527027`, for the commit you want to change. You can find this by using the `git log` command or going to [GitHub](https://github.com/) and finding it there.

Then we are going to use the interactive rebase function. So enter

```
git rebase --interactive '199c527027^'
```

Putting your commit id where I've got `199c527027`. Note the `^` at the end of the identifier. This tells git to start from the commit before the commit you care about.

The default editor will open and you'll see something like this.

```
pick 199c527 Add markdown extension to embed tweets in notes
pick 34d2aff Write note on embedding tweets in markdown
pick f0320a1 Rebuilt sqlite db 2023-01-20
pick 32fd58f make sure there is a h1 tag on note pages
pick aa0dalb images in notes should be max 100% width
```

This lists all the commits between the commit you care about and now - the latest.

Edit the line for the commit you are going to change. Change `pick` to `edit`.

Then save and exit (`esc` then `:wq` if in vi).

Now make your edits.

Once you've finished add the edited files. E.g. `git add <file-name>`.

Then run,

```
git commit --amend
```

This will replace the commit with your new one.

Then run

```
git rebase --continue
```

to complete the rebasing process.

Now you are done.

If you are pushing to GitHub you'll need to use the `--force` command. E.g.

```
git push -f origin main
```

