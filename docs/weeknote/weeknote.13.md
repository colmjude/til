---
title: "Weeknote #13"
tags: weeknote, dluhc, data-standards, versioning, chatgpt
author: Colm Britton
created: 2023/09/18
updated: 2024/03/24
---

## What I've done

This week has been really good. It felt like we achieved a lot and we finally built some momentum!

### Versioning

We implemented and rolled out versioning. Finally! [I even blogged about it](https://digital-land.github.io/blog-post/versioning-our-standards/).

Versioning has been on the cards for ages but we held off because a) we didn’t have the headspace to tackle it, and b) there are many moving parts.

Adam and I discussed a way forward when I was last in the office but last week was the first chance we had to make the changes. And this week, we had the chance to put it into action.

We could finally update 3 specifications ([conservation-areas](https://digital-land.github.io/specification/specification/conservation-area/), [article-4-directions](https://digital-land.github.io/specification/specification/article-4-direction/) and [tree-preservation-orders](https://digital-land.github.io/specification/specification/tree-preservation-order/)). It is a game changer for us when it comes to productionising how we design data standards.

### Datasets editor

The team (Paul S and Adam in particular) have made great progress on the dataset editor tool. It is great to see these sketches of some initial flows becoming real.

![An image showing my desk with a blank sheet of page and various pens I'll need for my sketchnotes laid out around the edges](/static/images/notes/images/work/dluhc-dataset-editor-initial-flows-cropped.jpg)

The dataset editor is another thing that should make our lives easier - and force a few conversations about how certain things are managed and by whom.

### Modelling data

We also drafted a data model for Nationally Significant Infrastructure Projects (NSIP). It is quite similar to the planning-application process:

* An application of some sort goes in.
* A series of steps are followed to decide whether it gets the okay or not.
* A decision is made and published.
* At this point it can be challenged.

This meant we could lean on the work we’d done there and, luckily enough, with some tweaking, [the specification](https://digital-land.github.io/specification/specification/infrastructure-project/) looked like something that could work.

It’s an encouraging sign that we can repurpose an existing pattern for another planning consideration. Having a set of repeatable patterns is precisely where we want to get to.

Fingers crossed it tests well with real data.

## What I’ve learnt

When I tried to push a new note to my site this week, I got an error. 

When `ssh` and `scp` work, they work. When they don’t, I’m completely stuck. Luckily, putting the error message into [ChatGPT](https://chat.openai.com/) gave me simple steps to fix it.

Thank you ChatGPT 🙏

I also used ChatGPT to customise the URL a locally running site is served on using Python’s `http.server`. 
I didn’t even know this was an option but spending countless hours messing around with asset paths prompted me to ask if there was a better way. Luckily, ChatGPT gave me the answer.

Well, that’s nearly true. It gave me a nudge in the right direction, and with a bit of googling, I got over the line. So now I can run our [specification repository](https://github.com/digital-land/specification) locally and serve it at localhost:8080/specification, mirroring how it is served on the digital land site (https://digital-land.github.io/specification).

[Code is here](https://github.com/digital-land/specification/blob/main/bin/server.py).

One failed attempt baking some oat biscuits later, and I now know wax paper and baking paper are two different things. Who knew.
