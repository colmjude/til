---
title: "Weeknote #16"
tags: weeknote, dluhc, data-standards, blogging, horizon, trello
author: Colm Britton
created: 2024/01/18
updated: 2024/03/20
---

*These “weeknotes” cover a bit of December and January.*

## Work

Here are a few highlights from the last few weeks:

#### Data modelling

We threw together some thoughts on [Site allocations](https://miro.com/app/board/uXjVN9NnfDc=/).

We did something similar for [Gypsy, Roma and Traveller sites](https://miro.com/app/board/uXjVNIiMA2Y=/).

And shared a third [board on Housing target numbers](https://app.mural.co/t/mhclg2837/m/mhclg2837/1706095948277/891b2a8b49ac90e143ea03e40ffd70134227e490?sender=u0a3f3dbf2e64a1ee0ea83028).

#### Our process

I published a blog post about [our data standards design process](https://digital-land.github.io/blog-post/our-data-standards-design-process/). We’ve purposely split the process into clear stages so that its easier to report on progress and see where things are getting stuck.

We’ve started producing [a diagram showing the number of planning considerations in each stage of our process](https://github.com/digital-land/data-standards/blob/main/assets/images/data-standards-progress-jan-18th-2024.jpg). I wrote a quick script to output the numbers, which I then use to update the diagram.

I must be able to make the script update the diagram too. One to look into.

#### Emerging pattern

We started using meaningful field names for any significant dates in our data models. It feels like an [emerging pattern](https://standards.planning-data.dev/patterns/contextual-dates/). Using meaningfully named fields helps reduce the ambiguity of date fields.

Using `start-date` to mean different things in different contexts was confusing. An alternative is fields with meaningful names. If data providers recognise the names of fields, if the names are their language, then it is easier for them to provide the data.

For example, the [tree preservation order dataset](https://digital-land.github.io/specification/specification/tree-preservation-order/#tree-preservation-order-dataset) has `made-date` and `confirmed-date`. These are important dates in the world of tree preservation orders. Updating the data model to reflect this made it easier to provide the data and improved the quality of the records.

#### Data

We finally updated the [permitted development right data](https://www.planning.data.gov.uk/dataset/permitted-development-right). Going through the legislation was a slog, but we finally got there 😮‍💨

## Other stuff

#### Trello

I’ve been trying to use trello more effectively.

At work, that means using EPICs that lead to smaller tickets, using “Done when” checklists, including other tickets as checklist items, and linking various tickets and boards. It has been helpful so far, but time will tell if this has been a good investment.

At home, Vanessa and I use trello to manage the mountains of life admin. Using trello means we have a dedicated space for the ‘business’ talk. Keeping it contained to trello should be good on the wellness front.

As an aside, I wish it was possible to create tables in trello tickets. Trello accepts markdown so I’m not sure why it doesn’t. Shame.

#### Wise + Monzo

I'm a big fan of [Monzo](https://join.monzo.com/c/xhl5zs2) at the best of times, but I recently discovered that making international payments with Monzo is really easy. It uses [Wise (formerly TransferWise)](https://wise.com/invite/dic/colmb15) under the hood, so if you already have an account with Wise, it is a doddle.

A tip I’ve learnt is to add recipients on [wise.com](https://wise.com/invite/dic/colmb15). Then go back to Monzo to make the actual payments. The reason is that there are more options to set up a recipient on Wise, whereas the UI in Monzo is a little limited.

An added bonus, if you are a Monzo pro account holder, is you'll earn cashback on all international transfers you make through the Monzo app.


## What I’m reading / thinking about

[The horizon scandal](/notes/opinion/post-office-horizon-scandal). It is disgraceful.
