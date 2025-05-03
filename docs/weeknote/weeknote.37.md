---
title: "Weeknote #37"
tags: weeknote, okrs, planning, data design, process
author: Colm Britton
created: 2025/03/31
updated: 2025/04/14
---

_Week beginning 31st March_

Week 1 post the mad dash to the planning application finishing line.

This week I resurfaced from the planning applications hole and re-engaged with the wider data design activities—item 1 was to help plan for the upcoming quarter.

Some big team changes are happening across the programme that we’ll need to align with. Big shifts that will shape how we work and what we prioritise.

And, sadly, we said goodbye to [Adam](https://www.linkedin.com/in/adamshimali/)—a superstar developer and all-round fountain of knowledge and pragmatism. That’s going to be a tough one to bounce back from.

### Q1 planning

Despite the changes, we’ve managed to develop a **coherent set of OKRs** that reflect the current shape of the team. They focus on two main things:

#### 1. **Improving the data design service through research and refinement**

Until now, our data design process has emerged organically—shaped by the work we’ve done on planning considerations. We've built some tooling to help with repeatable tasks like capturing required information and reporting. But, it’s functional at best. It was thrown together around loosely defined internal needs and has served that purpose.

This quarter, we want to take a breath and ask:

- How well is this actually working?
- Can others follow or contribute to the process?
- What does good look like for our users?

We’re aiming to support both **internal teams** (like policy colleagues) and **external collaborators**—others working in the same space who we’d love to see producing similar outputs using our materials and methods. Essentially, the way they interact should be similar; it's supposed to be an open process after all.

There’s been talk of a **“self-serve” model**, but I’m not sure that’s quite the right term. It’s more about making the process understandable, open, and usable. And useful beyond our team.

#### 2. **Continuing work on the planning application data specifications**

What we’ve delivered so far is a solid start—but very much a start.

We’ve [published draft specs](https://github.com/digital-land/planning-application-data-specification?tab=readme-ov-file#application-types), yes—but validating and testing them is just starting. And that's before we get onto using them as a platform to improve things.

That will take time and no doubt lead to more work. Just last week, the advisory group flagged the value of **validation rules**—something we agree would be useful, but it’s definitely not a quick task.

We’re also grappling with a shift in operating model: moving from systems designed around paper forms (including when digitised) to ones that are led by structured data specifications. It’s a big change, and one that won’t happen overnight. There's lots to work out.

Beyond that, we’re starting to look at the specifications for parts of the process after submission, like:

- what data should be published when a decision is made
- a data model for planning conditions
- data specifications around CIL, Section 106s, etc

We’ve made a start on identifying these but as ever we are just looking at it from one angle so if anyone has any suggestions or thoughts we'd love to hear them. I imagine there will be  a long tail of planning application-related specs we’ll need to work on.

Planning applications aren’t going away anytime soon.

#### Bonus OKR 3

As well as the initiatives above theres always another OKR related to working on more specifications for data that should be on planning.data.gov.uk

We expect to make progress on specs in other areas of planning where the planning need is well understood and there’s community interest—for things like **site allocations** and **housing numbers**.

The idea being they’ll help us keep momentum while showing how the data design process can scale to different parts of the planning system.

### Planning applications

Even while shifting focus back to wider data design work, I managed to make a bit of progress on planning applications.

I had one request for a complete specification file. So I created [a specification index file](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/index.md) that has everything in it.

I presented to the ODP early adopters group—this is the group we hope will help us validate and test the specifications.

Some interesting things came up.

One big question was about UUIDs (needed as the `reference` in the specification).

Essentially, we need a reference that everything can hang off—but I recognise it also has to work for people within their current processes.

We’re definitely not suggesting LPAs stop creating their own readable, recognisable internal references (which might even be used openly).

But we do need a **system-wide ID** that’s unique and stable, even as an application moves between systems.

See [issue #227](https://github.com/digital-land/planning-application-data-specification/issues/227) for more information on IDs.

Another point was re application fees (see [issue #228](https://github.com/digital-land/planning-application-data-specification/issues/228)).

I’d included `fee` in the application model—for two main reasons:

- both Planning Portal and PlanX have it in their schemas
- some checklist sections clearly state that fee is a required

But a great point came up in discussion: this might be too limiting in a data specification because it could:

- stifle innovation by making it harder for other organisations or services to programmatically submit applications
- lead to problems with organisations "marking their own homework" - even if the rules for calculating fees are open and machine-readable, asking applicants to submit the fee amount might lead to errors or more work for planning officers

Anyway, plenty of food for thought. And shows, as I said above, the planning application data specs are not done 🤣
