---
title: "Weeknote #41"
tags: weeknote, planning applications, planning requirements, visuals
author: Colm Britton
created: 2025/05/12
updated: 2025/06/01
---

*Weeknote covering 1-12 May*

We’re still waiting for more feedback on the planning application specifications, so this week I’ve focused on work around the edges.

## Planning requirements

We’ve been looking into planning requirements; documents or supplementary information that form part of a planning application. They’re sometimes referred to as _information requirements_.

We’ve started building a dataset of all known requirements so that:

- there’s a single, consistent list (people currently use different names for the same thing).
- we can begin recording the rules as data, for example, "All full applications must include planning requirement X."

Every requirement depends on the type of application. Some apply across the board (like “a completed application form”), but most are more specific. There are four main scenarios:

- National requirements
- Conditional national requirements
- Local requirements
- Conditional local requirements

I've started to put together the data for the [national requirements](https://github.com/digital-land/planning-application-data-specification/blob/main/data/national-planning-requirement.csv), for example
```
full-site-plan,full,,site-plan,2025-05-06,,
```
This says for all "full" applications a "Site plan" is required.

This approach allows systems to determine what’s required using a shared set of rules. For example, just from the application type alone, we can already tell that for a full planning permission application, the applicant needs to provide:
```
Arboricultural impact assessment
Biodiversity survey and report
Elevation - existing
Flood risk assessment
Land contamination assessment
Landscaping plan
Location plan
Noise assessment
Roof plan - existing
Site plan
Statement of community involvement (SCI)
Sustainability statement
```

View [the set of national requirements](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-requirement.csv) that have been captured so far.

## Visual explainers

We’ve been having a lot of conversations about things we need to explain better. Questions like:

- What is the data design offering?
- How do open data and open standards improve the planning system?
- How are the planning application specifications meant to work and why do they matter?

To answer those properly, we’ve realised we need more than just words. We need visuals to help tell the story.

I’m a strong believer in the power of visuals. They can make complex systems easier to grasp. But good ones take time. And that’s the tricky bit right now. A quick 15-minute sketch won’t cut it.
#### Explaining our approach to planning application specifications

At a high (and grossly simplified) level, the planning system is what sits between a person’s **need to build something** and their **permission to build it**.

And for many people, that system feels like a black box.

![top-level@2x.png](/static/images/notes/work/top-level@2x.png)

We can unpack that further by showing how a user (usually the applicant) puts information into the system, and what they get back. Again, this is deliberately simple. That’s the point.

![planning-permission-in-out@2x.png](/static/images/notes/work/planning-permission-in-out@2x.png)

There are three key stages here:

**1. Submission service**

Someone wants to build something, for example, a home extension, a new flat, a shop. To do that, they need permission.

They submit a planning application, expressing their need in a format the system can understand.

This might be a paper form or a digital service like Planning Portal.

**2. Deliberation** _(still debating the name)_

The application enters the system, specifically, into a planning authority.  

A lot happens here, including:

- **Validation** (is the application complete and correct?)
- **Consultation** (with statutory consultees, neighbours, etc.)
- **Determination** (assessed against policy, using professional judgement)

**3. Decision**

A decision is made; granted, refused, or granted with conditions.  
It’s published. The applicant is informed and now knows whether they can proceed.

Already, these two diagrams help show why we’ve put so much time into the **planning application submission specifications**.

It’s the start of the process.

If we improve the quality, structure, and consistency of what goes in, we improve the chances of getting better outcomes.

I think of it like this:

> **Better inputs lead to better decisions, fewer delays, and better data flowing through the system.**

That’s what the planning application data specifications are trying to achieve.

![submissions-specs@2x.png](/static/images/notes/work/submissions-specs@2x.png)

But to make the system really flow, we need to improve both **what goes in** and **what comes out**.

That’s why we’re now picking up the **planning applications and decisions specifications**.

![submissions-and-decision-specs@2x.png](/static/images/notes/work/submissions-and-decision-specs@2x.png)

IIf we can raise the quality of inputs and outputs, and make sure those two parts align, we create the conditions for a clean, consistent, end-to-end data flow.

That’s the plan, anyway.

---
## Other bits and bobs

**Teaching CS and AI skills**

CEOs from some of the biggest tech firms in the world are getting behind a push (called [CSforALL](https://csforall.org/unlock8/open-letter)) for CS and AI skills to be taught in schools so that the next generation become AI-native.

Interesting stat
>Just one high school computer science course boosts wages by 8% for all students, regardless of career path or whether they attend college.

I wonder if there is a similar initiative in the UK?

**htacess**

My site broke, so I had to fix it by tweaking the `.htaccess` file. Not exactly my comfort zone, but I got it working. I wrote down what I did too—so when it inevitably breaks again, I’ll at least have a record to go on.

**Geospatial fun**

Alasdair Rae shared his Greggs steak bake spidermap 🔥
https://github.com/alasdairrae/alasdairrae.github.io/tree/master/steakbakespider
