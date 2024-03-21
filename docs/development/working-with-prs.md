---
title: "Working with PRs"
tags: git, development, snippet
author: Colm Britton
created: 2020/07/02
updated: 2024/03/21
---

## Testing locally

Sometimes people will fork your repo, make some changes and submit a pull request. You'll then want to test the pull request locally before accepting/merging.

To do that I do the following

    # create a new branch
    git checkout -b <branchname>
    # or (with alias)
    git cob <branchname>

    # then pull the PR into this new branch
    git pull origin pull/<PR id>/head

I'm not sure if there is a better way but this approach has worked for me in the past. I got this from this [stackoverflow thread](https://stackoverflow.com/questions/5884784/how-to-pull-remote-branch-from-somebody-elses-repo).

## Adding commits

You might need to make a commit of your own to add to the pull request (PR). Make your changes and commit to the branch you are working as you normally would.

Then push commit to the PR using:

```
git push origin <local_branch_name>:<remote_branch_name>

# for example
git push origin descriptions:gwencariad-patch-1
```

That works if the PR branch is already in the main repo. If someone has forked your repo, made some changes and raised a PR then you'll need to follow these steps:

First, add a new remote to the fork of the repo
```
git remote add <remote_name> <url_to_fork>

# For example
git remote add pipwilsonrepo https://github.com/pipwilson/digital-land.github.io.git
```

Once you've set that up you should be able to push to it (if the repo is public and allows write access)
```
git push <remote_name> refs/heads/<local_branch_name>:refs/heads/<branch_name_on_remote>

# For example
git push pipwilsonrepo refs/heads/feed:refs/heads/add-atom-feed
```

## Cherry picking

Turns out you can also cherry pick commits from a PR. This might be useful if you miss a PR and have made some of the same changes.

To cherry pick a commit

    git cherry-pick <commit_hash>
