---
title: "Share a site you have running locally"
tags: webdev, development, sharing, testing, prototyping
author: Colm Britton
---

Install [localtunnel](http://localtunnel.github.io/www/)

    npm install -g localtunnel

When you have a site served locally, using something like the python http server, run

    lt --port <port>

Where `<port>` is replaced with the port of the local server. Usually 8000 or 8080.

The site is then available over the internet for showing progress with colleagues or testing remotely.

You'll be given a URL to share. On the first visit a user will be warned about the site and need to press the blue button to continue.

