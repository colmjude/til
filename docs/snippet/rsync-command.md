title: Use Rsync to copy lots of files
tags: development, commandline, tip, til
author: Colm Britton
--------------------

**Rsync** is a more powerful **cp** commandline utility. It helps you replicate the contents of a whole directory, sub-directories included.

    rsync -a dir1/ dir2

This will copy everything in *dir1* into *dir2*.

The `-a` option means it will preserves symbolic links, special and device files, modification times, group, owner, and permissions.

`-r` is a an alternative option to `-a`.

### Useful options

`-n` or `-dry-run` always you to try it before actually doing it.

`-v` for verbose.

`-P` for partial and progress. Allows transfers/copies to be resumed.

`--exclude` allows you to exclude files from the transfer/copy. There are multiple ways to do it.

    # a pattern
    rsync -a --exclude '*.jpg*' dir1/ dir2
    # mutliple files to exclude
    rsync -a --exclude={'file1.txt','dir1/*','dir2'} dir1/ dir2
    rsync -a --exclude 'file1.txt' --exclude 'dir1/*' --exclude 'dir2' dir1/ dir2
    # list files to exclude in a file
    rsync -a --exclude-from='exclude-file.txt' dir1/ dir2

`--include` allows you to add back in a file you've excluded.

### Replicate on a remote server

rsync can be used between machines, as long as both have it available. This makes it useful for transfering files to a server.

    # local to remote
    rsync -a ~/dir1 username@remote_host:destination_directory
    # remote to local
    rsync -a username@remote_host:/home/username/dir1 place_to_sync_on_local_machine

### Further reading

[How To Use Rsync to Sync Local and Remote Directories on a VPS](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)
