---
title: "Weeknote #14"
tags: weeknote, dluhc, data-standards, versioning, chatgpt
author: Colm Britton
created: 2023/09/18
updated: 2024/03/18
---

*This “weeknote” covers September and part of October 2023.*

## Travel

We spent a relaxing week in the Seychelles 🏝️

That place is not real. It is picturesque, bordering on make-believe. It looks like a Pixar creation.

I’d love to go back one day, but I’m not sure my bank balance can handle it.

Padel has made it to the Island - that was surprising!

I also spent a week in London for work. That was full-on — worth it, but full-on.

## Work

We updated the [development plan specification](https://digital-land.github.io/specification/specification/development-plan/) and created [a prototype](https://development-plan-prototype.herokuapp.com/) to help us crowdsource some data.

The data model for development plans needs to handle a lot of nuances because local plans are rarely consistent. 

Geographies are a good example. In principle, every planning authority should have a local plan covering its jurisdiction. However, in reality, it doesn’t quite work that way.

We’ve learnt that:

* Every plan applies to an area. This area is mostly the same as the local authority boundary.
* Sometimes, the area is different from the planning authority boundary. There might be slight differences.
* Sometimes, planning authorities join forces and make a plan together. In these cases, again, sometimes the area will be the union of the planning authority boundaries, but sometimes it won’t.

For the prototype, we wanted to make it easy for people to provide a geography for the common case → the area = planning authority boundary. 

So, in the background, we selected the planning authority geography from data available on planning.data.gov.uk and displayed it on a map. We then asked users to confirm if this is correct instead of asking them to upload it every time.
We thought that’s got to be easier, right? 

Turns out that to the untrained eye looking at a local plan, it is pretty difficult to be sure what area it covers. Therefore, most users skipped that part 🤷‍♂️

*Note: we couldn’t get people with that localised knowledge in the room.*

The whole exercise reinforced that:

Local plans are complicated. Too complicated for a layman. Everyone does them differently, and there is only a vague air of consistency.

We finally published [changelog pages](https://digital-land.github.io/specification/specification/tree-preservation-order/changelog) for our specifications, which is a big win for recording how the specs change over time.

We also made some progress on the data standards manual, including [listing all the fields we use across all the datasets](https://standards.planning-data.dev/fields/) used by or on the platform. [ChatGPT](https://chat.openai.com/) sped this up for me.

[Flood-risk-zones](https://www.planning.data.gov.uk/dataset/flood-risk-zone) and [infrastructure-project](https://www.planning.data.gov.uk/dataset/infrastructure-project) (Nationally Significant Infrastructure Projects - NSIP) data is now available on the platform.

## Other stuff

Back [in February, I said I was looking forward to Passkeys](https://colmjude.com/notes/weeknote/weeknote-8/) becoming a thing. Well, I’ve just started using one to log into Github 🥳

My prompt engineering (🙄) skills are improving. 
I recently entered a single prompt that got ChatGPT to spit out the Python needed to display the used and unused entity ranges for datasets on planning.data.gov.uk. Other than tweaking the output format, it worked exactly as I had hoped.

[The nitrate in bacon (and other meat products) is what makes it carcinogenic](https://www.theguardian.com/food/2023/sep/18/the-truth-about-nitro-meats-my-seven-year-search-for-better-bacon). This additive is mainly used to keep the meat pink so you’d think healthier alternatives should be available. Although not widespread, a few alternatives are coming to market. One is Finnebrogue Naked bacon. One to try next time I’m back in the UK.

When I was putting together a map component for the development-plan prototype, I dug out an old component I created a few years ago. I should've been able to just use it, but I couldn’t. I just couldn't work out what old me had done.

In the end, I hacked together a new leaflet-based map so we did have a map component, but I’m still confused about why I couldn't the other one working 🤔 It is like it was written by someone else. Is that normal?
