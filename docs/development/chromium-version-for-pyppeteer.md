---
title: "Updating Chromium version you use with pyppeteer"
tags: pyppeteer, chromium, screenshots, python
author: Colm Britton
created: 2023/02/12
updated: 2023/02/12
---

I was working on a simple screenshotting tool but noticed the pages weren't rendering properly in the screenshots.

The tool uses pyppeteer with the installed version chromium to open a url and take a screenshot at a given dimension.

Trying to work out what was happening I printed out a few details of the browser pyppeteer takes the photo in. I did that by adding

```
dimensions = await page.evaluate('''() => {
  return {
    width: document.documentElement.clientWidth,
    height: document.documentElement.clientHeight,
    deviceScaleFactor: window.devicePixelRatio,
    userAgent: window.navigator.userAgent
  }
}''')
print(dimensions)
```

Interestingly the userAgent it was using was
```
'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/71.0.3542.0 Safari/537.36'
```

And when I compared it will the userAgent return in the console in Chrome I got
```
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
```

Notice the different version on Chrome. `HeadlessChrome/71.0.3542.0` vs `Chrome/108.0.0.0`.

So I needed to update the version of Chromium pyppeteer used.

In [the docs](https://miyakogi.github.io/pyppeteer/reference.html) I noticed you could set an environment variable (`$PYPPETEER_CHROMIUM_REVISION`) to update the version of Chromium to use.

I also used `print(pyppeteer.__chromium_revision__)` in the script to print the version it was using. It gave me `588429`.

I tried to set this variable in a `.env` and load it up with [python-dotenv](https://pypi.org/project/python-dotenv/) but that didn't seem to work.

So I then decide to set it in the terminal shell I was using to run the script from. Just to see what would happen.

I used [this index](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac/1000090/), manipulated the url to find a newer version number and ended up with `1000090`.

I then set the variable in the terminal with 

```
export PYPPETEER_CHROMIUM_REVISION=1000090
```

And, then re-ran the script. This time it downloaded and install the newer version. And when it took the screenshot it was a mirror image of what I see in the browser.

The `userAgent` output was
```
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/103.0.5046.0 Safari/537.36'
```

But the output of `print(pyppeteer.__chromium_revision__)` was still `588429`.

I ended up having to set the enviroment variable in my `.zshrc` file. That was the only way I could get it to work each time.
