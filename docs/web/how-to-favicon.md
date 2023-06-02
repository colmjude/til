---
title: How to favicon
tags: web, development, design, brand, how-to
author: Colm Britton
created: 2023/01/13
updated: 2023/01/17
---

Favicons have always been one of those things I don't like doing.

You don't have to do it often but when you do what you need to do has changed since the last time you did it and, in general, it is a faff.

I recently added one to the [learnbymaking site](https://learnbymaking.wales/en/) and still found it difficult to find the definitive truth follow along guide.

I ended up finding this [summary article from creativebloq](https://www.creativebloq.com/illustrator/create-perfect-favicon-12112760) very useful as a general guide. I also found [this guide from evilmartians](https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs) helpful in terms of getting into the details.

It's still not clear to me whether you definitely need a `.ico` favicon or if it's fine to have `favicon.png`. In the end I went with `favicon.ico` because it felt like the safest bet.nIf you have `.png` version you can convert it to `.ico` using a tool like [faviconer](http://faviconer.com/icon/index).

### What images to create

I created a favicon at these sizes:

* 16x16
* 32x32
* 48x48
* 180x180
* 192x192
* 512x512

To make that easier I created this [favicon template file for illustrator](/static/resources/favicon-template.ai).

I also saved the 512x512 icon as an `.svg` which is used by Safari browsers.

### Markup

I added this markup to the `<head>` of each page on the site.

```
<!-- favicon tags -->
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon" />
<link rel="icon" href="/assets/images/favicons/lbm_favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/images/favicons/180x180.png">
<link rel="manifest" href="/manifest.webmanifest">
```

And, created a `manifest.webmanifest` file containing the following.

```
{
  "icons": [
    { "src": "/assets/images/favicons/192x192.png", "type": "image/png", "sizes": "192x192" },
    { "src": "/assets/images/favicons/512x512.png", "type": "image/png", "sizes": "512x512" }
  ]
}
```

And it all seems to be working ok. You can use [SEO site checkup](https://seositecheckup.com/analysis) to check it picks up a favicon.
