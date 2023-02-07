title: "Weeknote 30th Jan 2023"
tags: weeknote, matter, thread, learnbymaking, flask, sketchnotes
author: Colm Britton
created: 2023/01/30
updated: 2023/02/07
--------------------

I’m publishing these weeknotes on the Tuesday after the week in question finished. I was very close to giving up on them but forced myself to publish something.

It was a pretty busy week. It felt like it was anyway. I was solo daddying for part of it so that kept me on my toes.

## Revisiting a side project

This week, I revisited a side project I last looked at in 2020. I say revisited, but the main goal was to get it running again. Which I just about managed.

Part of requires a user to upload a file. I was using [flask-uploads](https://pypi.org/project/Flask-Uploads/) for this but that is no longer maintained. Thankfully, the ever-helpful Miguel Grinberg has [a very helpful tutorial on adding file uploads to a flask project](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask).

Part of the application uses JS template literals to render JSON returned by the server. This week I learnt it is possible to use expressions and therefore ternary operator expressions within template literals. Very handy. I added [a note on how to use them](https://colmjude.com/notes/snippet/js-snippets/).

## A learn by making handover

I spent some time handing over the [learnbymaking tools](https://learnbymaking.wales/en/updates/2022/12/21/making-tools-for-learn-by-making.html) to the folks at CDPS.

Inevitably this meant demoing them. And, inevitably, it did not go to plan 🫣

Eventually, I figured out what had happened but it was an uncomfortable 45 mins that felt like eternity.

I had included a `package-lock.json` file in the [prototype kit](https://github.com/learnbymakingwales/lbm-prototype-kit) we used for labs. I’d done this because without it (without specifying the package versions), it would not work on [GitHub CodeSpaces](https://github.com/features/codespaces). For participants with restricted access to their machines, using CodeSpaces was a must.

The issue was since we’d run the labs - and therefore, last used the prototype kit with CodeSpaces, I had updated the [lbm-frontend package](https://github.com/learnbymakingwales/lbm-frontend). However, this package is not published on [npm](https://www.npmjs.com/). It is installed from github using [gitpkg.now.sh](https://gitpkg.vercel.app/).

All fine, except when you include a `package-lock.json` file pointing to a specific version of your package installed by gitpkg and you’ve made a change to the package. I imagine the `integrity` attribute of the entry is not going to match.

Anyway, I fixed it by removing the entry from `package.json`. I should work out why the latest versions of all the packages won’t work on CodeSpaces but I needed to fix it quickly so we could continue with the handover.

## Matter and thread

I spent a bit of time getting my head around Matter and Thread. Basically, the future of "smart homes" and hopefully, the things that finally make the “smart home” a useful and not just a gimmicky thing.

My understanding is [Matter](https://www.theverge.com/23390726/matter-smart-home-faq-questions-answers) is the standard. So how devices communicate, how they speak the same language. For example, if one device (e.g. the controller) says “switch the light on” then the receiving device will know to switch the light on. What this means is we won’t be buying bulbs that work with Amazon devices and different bulbs to work with Apple devices. Any (controller) device should work with any bulb.

And [Thread](https://www.theverge.com/23165855/thread-smart-home-protocol-matter-apple-google-interview) is the protocol they communicate on and create a local network. This means devices can communicate with each other (e.g. I’ve spotted motion so you switch your light on) - all on a local network (not over the internet). This local network also means low-latency (things should happen quicker - no lag when switching the little on) and low-power (battery-powered devices that only need to power up briefly when they need to communicate something).

Apparently, it should also mean easier setup - it should happen automatically, so no more repeatedly adding this device to this controller and WiFi credentials. Please let that be the case.

## Sketchnotes

I didn’t spend as much time as I would have liked on the Sketchnotes course but I did like one of the ideas covered. The idea of having and practising a library of components. It seems too obvious - we do it all the time with code and UIs so of course it should work with sketchnoting too!
