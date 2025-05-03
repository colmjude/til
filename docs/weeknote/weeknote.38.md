---
title: "Weeknote #38"
tags: weeknote, pdrs, data layer, service layer, dates
author: Colm Britton
created: 2025/04/17
updated: 2025/04/24
---

_This weeknote covers the week beginning 7 April_

Not much to say about planning application work this week—because, for once, I haven’t spent that much time on it.

I’m off on holiday next week, so most of the week has been about clearing decks and finishing off other bits and bobs.

### Historic permitted development rights (PDRs)

I spent some time looking into an interesting problem involving **historic Permitted Development Rights (PDRs)**.

Over the years, multiple Acts, Statutory Instruments and Orders have changed or amended the PDRs. But some Article 4 Directions (A4Ds) still reference the older PDRs—ones that may no longer exist in the same form.

Previously, we were approaching this by asking:

> _Can our data model accommodate historic PDRs as-is, or do we need to tweak it?_

But now I think there's a more fundamental question:

> _How are these historic PDRs actually being used?_

In other words—what is the user trying to achieve? What is the **data need**?

Which, as ever, takes us back to questions of **law, legislation, and policy**.

- are these old A4Ds still valid?
- do we need to trace the history of a PDR through the legislative changes to understand whether it still applies?
- or are they now invalid, since the thing they reference no longer exists?

It’s a good example of where understanding the legal context and data modelling have to go hand-in-hand.

Kieran has done a good write up of what we've learnt so far and shared it in the [PDR discussion](https://github.com/digital-land/data-standards-backlog/discussions/39#discussioncomment-12867502).

### Dates in data vs dates in services

Someone asked this week why we ask for dates in the **YYYY-MM-DD** format. Honestly, I had to pause and remind myself.

We’ve been using that format for so long, it’s just second nature now.

I ended up writing a response—so next time the question comes up, I’ll have something to point to.

It also reminded me how important it is to explain the difference between:

- the **data layer**, where systems exchange machine-readable information (like ISO dates), and
- the **service layer**, where humans interact with that data in more familiar ways

When we’re working on data specifications, we’re operating at the data layer. But it’s easy to forget that most people are used to seeing dates as part of a user interface, not a schema.

Take your favourite news site or social feed. Dates might show up as:

- _“23rd March 2023”_
- _“2 hours ago”_

That makes sense to us—but behind the scenes, it’s stored in a machine-friendly format so systems can exchange and use it consistently. It’s the service that translates it into something more human.

I think there's more to say on this.

### Non-work – life

#### **Trello got an inbox**

[Trello](https://trello.com/) have launched an inbox feature so you can email things in and turn them into cards. I’m honestly surprised they didn’t have this already.

You end up with a list of cards that you can then drag into your boards. It’ll be interesting to see how well it works—and whether the **Atlassian Intelligence** (AI—get it?) can do anything useful, like summarise emails.

You can send things to the generic address: `inbox@app.trello.com` (or use your personal one 🤫).

I think it'll be a handy addition.

#### In global events...

Trump has trashed our retirement plans.

