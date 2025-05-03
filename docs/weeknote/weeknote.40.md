---
title: "Weeknote #40"
tags: weeknote, mhclg, planning applications, planning data, data design, process
author: Colm Britton
created: 2025/05/03
updated: 2025/05/03
---

*This weeknote covers the last 2 weeks of April*

Other than being severely hampered by a foot injury, it’s been a good, thought-provoking couple of weeks.

Definitely more conversation than doing—but they’ve been useful chats, and well-timed too (write-up debt aside 😅).

### Refining the process

One month into Q1 and we’re still working out the best way to tackle our objectives—and what’s most valuable to take on this quarter.

After being so deep in the planning applications work, coming up for air has surfaced lots of learning. Things we should do something about—especially around refining the data design process and how we make our outcomes more effective.

Some of the questions on my mind:

- **How should the process change now that we know more?**
- **How do we assess whether the data we’ve got onto planning.data is actually useful/right?**  
    Had a great conversation with Claire that got us asking: what do we do when the data _is_ on the platform, but doesn’t quite meet real planning needs?
- **How do we work more effectively with teams outside the department?**  
    Still working through this, but the community-led approach we took on planning apps seems like a good starting point. Feels like it’s about better understanding the landscape _and_ having dedicated community managers to support partnerships, local authorities, and other stakeholders.
- **What should handovers look like?**  
    Do we actually know enough about what other teams need from us? A good example: how does data design support the mandating of specifications under LURA? I’m not sure we have that clear yet.

I could go on—but I might overwhelm myself 🤣

### Planning applications

Feels like a lot of what we’ve done so far is the easy bit—the baseline. It’s just the beginning. Etc, etc.

While we wait for more feedback on the draft specs, a few other bits have started bubbling up and getting some focus:

* **What comes next?**  
	Submissions are just one part of the planning process. There are loads of other areas that could benefit from specifications. Our resident development management expert, Elliot, has been helping us map that out.
- **How does the current operating model need to change?**  
    If we’re going to be data-spec-led, we can’t just update forms without updating the specification alongside. How do we support the department to do that?
- **How should the specs evolve?**  
    I’m thinking about this on two levels:
    1. A guided approach—where we keep monitoring and working through community-raised issues.
    2. An extension model—where specs can grow in a federated way. If an extension is popular and gets adopted in multiple places, maybe it becomes part of the core.  
       I’ve even set up a demo repo to sketch out how part of that could work (see [extension-digital-site-notice-module repo](https://github.com/digital-land/extension-digital-site-notice-module)).
- **How do we keep the community engaged across all these strands?**  
    Up to now, we’ve managed because there’s been one central focus—baseline the specs. But with multiple strands emerging, maybe it’s not our job alone to hold that engagement.

As ever, there's that niggling question: _Are we getting this in front of enough people? Have enough voices been heard?_

This needs to work for everyone, and it has to fit into the existing system. The earlier we hear about issues, the better.

The good news is—it’s gaining traction.

We published a blog post:  
👉 [Get involved: validating the baseline planning application data specifications](https://mhclgdigital.blog.gov.uk/2025/04/17/digital-planning-get-involved-validating-the-baseline-planning-application-data-specifications/)

And there’s been some nice coverage too:  
📰 [MHCLG sets draft data standards for planning applications – UKAuthority](https://www.ukauthority.com/articles/mhclg-sets-draft-data-standards-for-planning-applications/)

---
## Other bits and bobs
#### A new design principle 🌱

After all this time, an 11th design principle has been added to the [Government Design Principles](https://www.gov.uk/guidance/government-design-principles):

> Minimise environmental impact

That’s pretty cool.

It gives designers the mandate to consider environmental impact as a core part of service design—not just a nice-to-have or personal concern, but something officially backed. It’s now part of the process, not outside it. 🔥

#### Learning by doing: Pydantic models

Finally had to learn what [Pydantic models](/notes/development/pydantic-models) actually are—beyond just nodding along when someone else mentions them. Turns out they’re really handy.

Thanks to that, the [export of planning consideration data](https://github.com/digital-land/planning-data-design/blob/main/data/planning-considerations.csv) now includes a `tags` field, with associated tags nicely serialised and separated by `;`.

#### Openness over certainty

I read an [interesting post from Anna Dorn](https://blog.medium.com/science-isnt-about-certainty-it-s-about-openness-c86708456059) on the Medium blog. I found myself nodding along to a lot of it. A few standout quotes:

> CEO [Matthew Gilpin](https://medium.com/u/44824841714c?source=email-5e06b7559e69-1745484726025-newsletter.v3-15f753907972-c86708456059-----------------------bf8bed41_434c_4d1e_8809_6d18ada8ed7f--------bf3f56c7deec) points out in a [recent piece](https://medium.com/brain-labs/when-following-the-science-can-be-anti-scientific-1c8a3fd88067?source=email-5e06b7559e69-1745484726025-newsletter.v3-15f753907972-c86708456059-----------------------bf8bed41_434c_4d1e_8809_6d18ada8ed7f--------bf3f56c7deec), progress doesn’t always mean breakthroughs.
> 
> Sometimes it means admitting you were wrong. Sometimes it just means saying, “I don’t know.”

> Siegel is right that consensus exists for a reason. Gilpin is right that it can harden into orthodoxy. The tension between those two truths — that consensus is necessary, but never final — isn’t a flaw. It’s the point.

> The real scientific mindset isn’t about knowing what’s true. It’s about staying open to what might be.

#### OpenAI eyeing Chrome?

Apparently, [OpenAI is interested in acquiring the Google Chrome browser](https://chromeunboxed.com/openai-and-perplexity-are-both-eyeing-chrome-if-google-is-forced-to-sell/). Not sure if it’s true or noise—but if it is, that’s… quite interesting.

#### Geodata and deforestation

In geospatial data news: the [EU is requiring origin data to prove that produce hasn’t contributed to deforestation](https://www.nytimes.com/2025/04/24/climate/ethiopia-coffee-europe-deforestation.html)(💰).

A fine initiative in principle—but it’s creating major challenges for small farmers who don’t have access to the tech or expertise to comply, particularly in places like Ethiopia.