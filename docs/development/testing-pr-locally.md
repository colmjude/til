title: "Testing PR locally"
tags:
author: Colm Britton
created: 2020/07/02
--------------------

Sometimes people will fork your repo, make some changes and submit a pull request. You'll then want to test the pull request locally before accepting/merging.

To do that I do the following:

    # create a new branch
    git checkout -b <branchname>
    # or (with alias)
    git cob <branchname>

    # then pull the PR into this new branch
    git pull origin pull/<PR id>/head

I'm not sure if there is a better way but this approach has worked for me in the past. I got this from this [stackoverflow thread](https://stackoverflow.com/questions/5884784/how-to-pull-remote-branch-from-somebody-elses-repo).
