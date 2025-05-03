---
title: "Weeknote #35"
tags: weeknote, planning applications, data modelling, tooling, codelists, podcast, open-working
author: Colm Britton
created: 2025/02/24
updated: 2025/03/01
---

_Week beginning 24 Feb_

Another week heavily focused on the planning application data specification work.

### Types and sub-types

We tackled the challenge of application types and sub-types (see [issue #158](https://github.com/digital-land/planning-application-data-specification/issues/158)). It turns out it’s not just the application type that dictates which modules need to be completed—a sub-type can affect that too.

We saw this in outline permission applications, lawful development certificates, and prior approval applications.

To handle it, we added an `application-sub-type` field to the **application type–module join table**. That means:

- modules common to all sub-types of an application type can still be handled with a single entry
- modules that are only required for certain sub-types can now be captured properly
    

Example: the **Materials** module is required for _outline: some matters reserved_ but not for _outline: all matters reserved_. So the entry is:
```
out-some-materials,,outline-some,materials,2025-03-03,,
```

See [line 207 of application-type-module.csv](https://github.com/digital-land/planning-application-data-specification/blob/main/data/application-type-module.csv#L207).

### Module - application type join data

Adding all the join records manually was getting tedious, so I built a quick tool to help.

Because the sections and forms were already queriable, I could cross-reference them with application types. I can input an application type and module name, and the tool will print suggested join records to the terminal—so I could review, tweak, and copy them into the CSV file myself.

### Issue types

We’ve started to open some issues that, if resolved, would mean stepping away from the current forms—which we promised not to do (yet).

They might be the right changes long-term, but we’re not sure they’re right **now**. We’re still developing the **baseline** specifications.

We've added them to a "[backlog](https://github.com/digital-land/planning-application-data-specification/issues?q=is%3Aissue%20state%3Aopen%20label%3ABacklog)" for now.

This is more of a note to self, but we’ll need to tell this story more clearly: the data model is separate from the eventual mechanism for collecting data. That could be a form—or a fully digital service.

As long as the right data is submitted, accepted by the planning authority’s back office, and helps a planning officer confidently assess the scheme, we’re good.

### Codelists

I’ve settled on _codelist_ as the name for the defined lists of values (see [last week’s note](https://colmjude.com/notes/weeknote/weeknote-34/)), enum just felt too technical, and have started fleshing them out. Eventually, there’ll be [a discussion thread for each one](https://github.com/digital-land/planning-application-data-specification/discussions/categories/codelist-enum).

### Advisory group page

I also published a list of [advisory group members](https://design.planning.data.gov.uk/advisory-group/members) on the site—for transparency. And, someone asked us to.

---


### Other stuff

I’ve been listening to a riveting podcast called [_Scam Inc.](https://www.economist.com/audio/podcasts/scam-inc)_ by _The Economist_. I'd highly recommend it. It dives into the huge, lucrative—and surprisingly professional—world of online scamming.

One scam it focuses on is called **_pig butchering_** (charming). The idea is to "fatten up" the target over time—building trust—before ramping up the scam. Wild stuff.

GDS posted about [a new resource to help people publishing to GOV.UK](https://insidegovuk.blog.gov.uk/2025/02/25/creating-the-gov-uk-publishing-design-guide/): the [Publishing Design Guide](https://design-guide.publishing.service.gov.uk). 
t’s pretty cool, and always great when teams share this kind of thing. It reduces duplication, helps others build on good work, and means more consistency for everyone. Another win for working in the open.

While I was having a look, I also stumbled across the [GOV.UK publishing component guide](https://components.publishing.service.gov.uk/component-guide)—another great resource worth bookmarking.

https://www.linkedin.com/posts/government-digital-service_weve-created-a-new-resource-the-govuk-activity-7300529232370122753-_WHU?utm_medium=ios_app&rcm=ACoAAAX9PjgBbX7F0ONEMY-fWRxLOPJY3clZCys&utm_source=social_share_send&utm_campaign=copy_link

