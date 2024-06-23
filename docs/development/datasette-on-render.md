---
title: "Datasette on Render.com"
tags: webdev, datasette, render.com, sqlite
author: Colm Britton
description: Get datasette working on Render
created: 2022/10/10
updated: 2022/10/11
---

I managed to get a datasette instance running on Render.com.

You need a python project that installs the `datasette` package. And you need the repo to include the sqlite db (e.g. `name.db`).

Then create a python **Web Service** on [Render.com](https://render.com/).

Set the start command to use datasette. I used

```
datasette name.db -h 0.0.0.0 --cors
```

Datasette usually uses `127.0.0.1` for the host but you can't use that (localhost equivalent) on Render.com.

Add the `--cors` flag if you want to be able to fetch data from the db from other sites. For example if you are [setting up free text search on your site like Simon Willison](https://24ways.org/2018/fast-autocomplete-search-for-your-website/) did.

--------------------

At on point [Simon wrote about deploying datasette to Glitch](https://simonwillison.net/2019/Apr/23/datasette-glitch/) so maybe one to try.
