---
title: "Weeknote #34"
tags: work, weeknote, planning applications, organisations, advisory group, recipe, copilot
author: Colm Britton
created: 2025/02/24
updated: 2025/02/25
---

*Covers week beginning 17 Feb 2025*

With the next advisory group fast approaching, I had to clear the decks again to focus on the planning application data specification work.

### Non-planning application stuff

Clearing the decks meant the start of the week looked like this:

- Created a schema for [Assets of Community Value](https://github.com/digital-land/specification/blob/main/content/dataset/asset-of-community-value.md?plain=1). We’ve still got [a few outstanding questions](https://github.com/digital-land/data-standards-backlog/discussions/100#discussioncomment-12110339) to resolve before it’s settled, but we’re getting there.
- Helped Adam with some wayfinding on the generic app. There’s a hierarchy to datasets in specifications—you can’t have supporting local plan documents if you don’t have the local plan, right? So we’ve been trying to make that clearer, especially when viewing parent records (like a conservation area) versus child records (like a conservation-area-document).
- Unpicked what needs to happen when organisations (especially councils) change. We dissolve them by adding an `end-date`, but that relies on someone noticing the change and updating the data. It needs documenting. Only then can we answer questions about what happens to related data—like the administrative boundary for a dissolved authority.

### Planning application data specifications

Mike and Liz have been designing and testing a lean coffee approach for the next advisory group session. I’ve been working through the modules—developing [information models](https://github.com/digital-land/planning-application-data-specification/discussions?discussions_q=is%3Aopen+label%3Acomponent), capturing issues, and suggesting where we can rationalise and flesh out the required codelists.

Side note: I’m never sure what the best label is for these defined lists. _Codelists_ and _ENUMs_ seem common, but neither screams plain English.

Drafting the information models has surfaced a lot of potential common components—plenty of near-repetition. And that's the key: _near_ repetition that needs working through. The challenge has been balancing the urge to untangle everything with the need to make tangible progress toward a workable set of specifications by the end of March.

The aim is to identify the common modules, structures, and fields while keeping the specifications flexible enough to accommodate variations by application type (and maybe sub-types?).

### What’s next (and what the advisory group is for)

- **Refine the codelists** – There are lots to work through, and it’ll take experts to flesh them out properly.
- **Tighten conditional logic for fields** – As we move from information models to specifications, we need to figure out how to capture these conditions as formal rules.
- **Validate module and field names, descriptions, and structures** – And ensure consistency throughout.

### Non-work – life

- Found this [stuffed flatbread recipe](https://www.drveganblog.com/cheese-and-potato-stuffed-flatbread/). Ticks the Addis-friendly, kid-friendly, and tasty boxes 😋.
- Got to witness a VVIP visit and the scale of what goes into organising one. Quite the operation.
- Errr, is this [a good move?](https://www.theguardian.com/technology/2025/feb/21/apple-removes-advanced-data-protection-tool-uk-government) Apple’s removed an advanced data protection tool in the UK. Not blaming Apple, btw.
- An article straight from the Mike Rose school of interesting: [a German judge ruled Birkenstocks aren’t works of art](https://www.theguardian.com/world/2025/feb/20/birkenstocks-are-not-works-of-art-top-german-court-rules-in-copyright-case).
- I’m remortgaging. Ouch.
- But I did use Copilot to code up a command-line mortgage calculator in about 30 minutes. Quite pleased with that.
