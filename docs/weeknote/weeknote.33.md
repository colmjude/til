---
title: "Weeknote #33"
tags: work, weeknote, planning applications, data specs, information models, data design, ai
author: Colm Britton
created: 2025/02/14
updated: 2025/02/15
---

*Covers week beginning 10th Feb*

Lots going on again.

### Highlights

- We got [Archaeological priority areas](https://www.planning.data.gov.uk/dataset/archaeological-priority-area) on the platform—our 50th geography dataset 🥳
- I've been working with Doncaster and Camden to prep a sample of their [planning conditions](https://digital-land.github.io/specification/specification/planning-condition/) data for [planning.data.gov.uk](https://www.planning.data.gov.uk/).
- Gwen and Maddie published a post about the recent [user-centred team day](https://digital-land.github.io/blog-post/user-centered-design-team-day/)—a long-overdue chance for designers across the teams to collaborate.
- Adam's making great progress with the [generic app for exploring and editing data for our specifications](https://github.com/digital-land/digital-land-application).

### Planning application data spec

I had to go dark for a couple of days to focus on the [planning application data specification work](https://github.com/digital-land/planning-application-data-specification).

Made solid progress developing the first set of "information models." It’s still not entirely clear how each should be structured, but the more I work on them, the clearer the shape becomes.

Roughly speaking, the key parts are:

- Module
- Fields
- Descriptions
- Application types
- Codelists
- Rules
- Requirement level
- Cardinality
- Issues

The hardest part? Staying focused on the first goal: baselining the existing application forms. That’s the commitment. But the tempting rabbit holes are everywhere.

### From data requests to desired outcomes

We've been reflecting on the last 6–9 months of data design work—what’s worked, what hasn’t, and the skills and capabilities required.

One big learning: teams often come to us with specific data requests, assuming they need to define the datasets themselves. This can lead to narrow solutions with limited utility.

It’s much more effective when teams focus on their **intended outcomes**—what they’re trying to achieve—rather than the data they think they need.

Less _“We need dataset X.”_  
More _“We need to understand Y to make decision Z.”_

### Other stuff

- Noticed a [Phil Hawksworth PR](https://github.com/denoland/docs/pull/1403) adding feedback/comments to a Notion database from a static site. Interesting option, if I’ve understood it correctly.
- FYI, the site uses [Lume](https://lume.land/)—an extremely fast static site generator. One to look into.
- The UK Government published their [AI playbook](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html). Good to see them stress that _"Human oversight is essential to ensure AI supports, not replaces, decision-making."_
- [If the AI Roundheads go to war with tech royalty, don’t bet against them](https://www.theguardian.com/technology/2025/feb/15/if-the-ai-roundheads-go-to-war-with-tech-royalty-dont-bet-against-them) – Some chase Artificial General Intelligence (AGI), no matter the cost. Others focus on solving specific problems—and they’re winning.
- [_The end of programming as we know it_](https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it/) – Tim O'Reilly wrote the piece I wanted to write. I've long said developers won't be replaced by AI anytime soon. If anything, these tools will open up programming to more people, leading to more software, more innovation, more jobs—just different ones. But O'Reilly says it all, with more history, expertise, and insight than I ever could. And that's just the start of the article—there’s so much in this one. Well worth a few reads!
