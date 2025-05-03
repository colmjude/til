---
title: "Weeknote #36"
tags: weeknote, planning applications, data modelling, specifications, tooling
author: Colm Britton
created: 2025/03/24
updated: 2025/04/03
---

_Second half of March 2025_

I’ve been holed up this week, deep in the **planning application data specifications** work.

We committed to sharing draft specs by the end of March, and I didn’t want us to let that slip and lose momentum—even though it’s been a massive piece of work.

But we got there 😅

### Compiled specifications

We published draft compiled specifications for [21 application type and sub-type combinations](https://github.com/digital-land/planning-application-data-specification?tab=readme-ov-file#application-types).

We’re calling them _compiled_ specs because, technically, there’s a spec for each of **84 components** (83 components and 1 application model). But that’s either way too granular to look at individually, or totally overwhelming if viewed all together.

So instead, the 21 compiled specs are grouped by what’s needed for each application type (and sub-type, where relevant). Hopefully, that's much more manageable.

### A bit of tooling support

To make life easier, I built a small **command-line interface** to help with some of the repetitive tasks.

It includes a few checks—for example, if you create a codelist but forget to assign it as _required_ in a module, it’ll catch that.

The code isn't pretty, but it saved my bacon.

And it should keep saving time: now, if any individual module changes, I can regenerate **all the compiled specs with a single command**. It’s just for generation—but still a big time-saver.


### Advisory group + community session

The advisory group session ran smoothly—and we repeated it on Friday for the wider community.

The **human-readable specs** (as opposed to machine-consumable ones) went down well. We got some good feedback straight away, especially about the `fee` field.

Right now, we’ve marked `fee` as a MUST. But it was pointed out that that might be too limiting.

The point that landed with me was: it could restrict who can build systems to submit planning applications—unless we also provide structured data on how to calculate fees and exemptions (something we are not planning yet anyway).

They gave the example of a housebuilder preparing lots of applications, who might want to submit them directly. Why not? But letting them specify the fee might be a bit like marking your own homework.

So... maybe not a MUST after all (see [issue #228](https://github.com/digital-land/planning-application-data-specification/issues/228)).

Slides and videos from the sessions are available on the [advisory group page](https://design.planning.data.gov.uk/advisory-group).

### Our approach to resolving issues

There were more [issues](https://github.com/digital-land/planning-application-data-specification/issues) than we could possibly resolve in the allotted time. And there are also issues that stray from our original goals:

* create a set of baseline specifications for submitting planning applications
* mirror the existing forms
* don't not break the current process

To handle this we had to handle as many as we could whilst being ruthless with what needs to be handled in a future iteration

### Next week

Next week, I’ll need to rejoin the wider world of **data design** and the **digital planning programme**.

Hopefully not _too_ much to catch up on 😬

---
### Non-work – life

There wasn't much time for non-work life this week.
