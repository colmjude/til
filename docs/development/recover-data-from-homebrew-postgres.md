---
title: "Recover your data from homebrew postgres"
tags: data, postgres, homebrew, commandline, development
author: Colm Britton
created: 2024/08/14
updated: 2024/08/14
---

I recently moved from a homebrew install of postgres to [postgres.app](https://postgresapp.com/) on the recommendation of a developer friend.

I jumped straight in and uninstalled the homebrew install with these commands

```
brew uninstall postgis
brew uninstall postgresql
```

Homebrew wasn't happy and asked me to uninstall a whole load of other stuff. I obliged.

I then [downloaded the postgres app](https://postgresapp.com/downloads.html) (btw, it comes with postgis) and followed the very simple setup instructions. Minutes later I had a working install of postgres again. Great.

When I connected to the postgres server, using [postico](https://eggerapps.at/postico2/).

At this point I realised my existing databases weren't available to the new postgres. Oooops.

To recover them, I first had to find the data directory for the homebrew postgres install. I eventually found it looking at the `homebrew.mxcl.postgresql.plist` file. This should be in your `/Library/LaunchAgents` directory (on MACOS).

I ran
```
cat /opt/homebrew/var/postgres/postgresql.conf
```

This file suggested the data directory was at `/opt/homebrew/var/postgres`.

To check, `ls` the directory and see if it has directories called `base`, `global` and `pg_*`.

### Reinstall homebrew postgres

First, stop the newly install postgres. There should be an elephant icon in your task bar. Click on it, stop the server and quit postgresapp.

Ideally, reinstall the specific version of postgres you had been using with postgres. For me it was version 14. So I ran

```
brew install postgresql@14
```

Then start the postgres server with

```
pg_ctl -D /usr/local/var/postgres start
```

### Backup existing databases

Now the old postgres server is running you should be able to access the old databases.

You can verify this and check what databases you have with
```
psql -U your_old_user -l
```

If you want to backup all the databases you can with
```
pg_dumpall -U your_old_user > old_pg_data.sql
```
Remember to choose a place to keep your backups.

Or, you can back up individual databases. This is the option I chose. Use this command for each database you want to backup

```
pg_dump -U your_old_user -d database_name > database_name.sql
```

### Restore databases

Now you've backed up all the databases you need to, stop the postgres server with
```
pg_ctl -D /usr/local/var/postgres stop
```

Then, restart the postgresapp server. Reopening postgresapp should do it.

Check you are using the new postgres install. I ran

```
psql -U your_new_user -l
```
and the list of databases was quite minimal so I knew it was the new install.

Then restore each database one by one. For each, you'll need to first create the database and then load in the data.

For each database, run
```
createdb -U your_new_user database_name
psql -U your_new_user -d database_name -f database_name.sql
```

If you had backed up all your databases in one you can restore it all with
```
psql -U your_new_user -f old_pg_data.sql
```

However, that replaces anything in your new postgres with the old stuff. That might be fine but I'd already started work on another database so chose not to.

Verify the data has been restored with 

### Clean up

The main thing to clean up is removing homebrew postgres again. You should be able to do that with 
```
brew uninstall postgresql@14
```

You can also clean up / remove the old data directory at `/opt/homebrew/var/postgres` but that is up to you.

Hope that helps.
