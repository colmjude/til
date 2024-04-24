---
title: "Weeknote #20"
tags: weeknote, roadmapping, reuse, prototyping
author: Colm Britton
created: 2024/04/06
updated: 2024/04/24
---

*This weeknote covers the last week of March and first of April. The Easter period.*

## Work stuff

I'm feeling good about the last couple of weeks. We have made real, tangible progress with the "considerations app" (a better name to come 🙏). Our progress means we are ready to switch off "The Grid" (a googlesheet that never got the better name it needed).

This is a big step.

### Just enough roadmapping

Talking about the considerations app, after doing some initial design work to bottom out what this app needed to do, we needed to build momentum and deliver value.

It was time for less talking and more doing.

So we did a bit of roadmapping. Not roadmapping in the sense of this is what we are going to do over the next X months but more:

* this is what we need to setup up the app
* this is what we need to get started
* this is what we need to do after that to turn something else off
* this is what we should then build so this application delivers more value than what we had before
* this is what we need to do next
* then we could do this
* and maybe this

![The output of our just enough roadmapping session. It has a series of stages or releases from left to right. Each release has a name or high-level objective, a rough definition or done and a summary of the impact. The content gets vaguer the further right we get on the roadmap](/static/images/notes/images/work/considerations-app-roadmap.png)

As you can see, the further along we went, the vaguer it got. That's fine. That's realistic.

We have a general direction of travel, and the first few steps are clear. We have enough to get going.

I like to call this just enough roadmapping. And it is the only type of roadmapping I'm game for.

### Reuse in action

One reason we are building this application to manage our work is to improve our reporting. We want it to be clear to users what has changed, when it changed and who changed it.

One thing people want to know has changed is when a planning consideration moves from one stage in [our design process](https://digital-land.github.io/blog-post/our-data-standards-design-process/) to another.
The first step is recording that information. The considerations app now does that.

We could've stopped there and told people we'd be able to report on that soon, but how useful is that? Instead, I prototyped a page showing how a planning consideration has moved through the design stages. But I only had a little time to spend on it.

We assume people want to see a timeline/changelog (we'll find out if that is true when we put it in front of people). I remembered seeing a timeline component from Moj Digital. I found it in their [design system](https://design-patterns.service.justice.gov.uk/) and thought it'd work for us. So, I went to [the Github repository for their frontend stuff](https://github.com/ministryofjustice/moj-frontend). Luckily, it was easy enough to understand, and I found the component.
A quick copy and paste later, and I had the scss I needed to replicate the timeline. Then, I needed the markup. I returned to the Moj design system, found [the timeline component](https://design-patterns.service.justice.gov.uk/components/timeline/), checked the example for the HTML and copied that too.
Squeezing the changelog data into the template took a few minutes and, boom, I was done.

![An image showing the timeline component recording when a planning consideration went through each stage](/static/images/notes/images/work/stage-changelog-timeline.png)

This is what I love about the x-gov design community. All this openly available stuff helps speed up your work. Big respect for everyone who shares stuff ❤️

## Other stuff

[Last weeknote](https://colmjude.com/notes/weeknote/weeknote-19/), I mentioned I'd written a script to output the notes I've published or updated in the last week. Who was I kidding 🤣 It's unlikely I'll write a weeknote every week. 

So, I updated the script to accept a `from` parameter. This way, I can easily see what I've published or updated over whatever period I choose. This is much more useful than before!

Notes published or update this weeknote are:

* [How to install non-npm node packages](/notes/development/npm-installable-package)
* [Weeknote #20](/notes/weeknote/weeknote-20)
