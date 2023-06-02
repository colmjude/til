---
title: Xargs command
tags: commandline, development, til, tip
author: Colm Britton
source: Jon Bramley
---

You can use the `xargs` command to pass the output of one command to another. Mind blown.

    grep -ir 10632f854d77def275091e2f9ac6a2c24d68bdbb97d23d5e5867934baffd5b66 collection/log -l | xargs rm

In this case I'm looking for all files named with the long hash in the `collection/log` directory. The command would normally list them all. Instead it gets `|` to `xargs` which then gives each line as an arg to `rm`. 
