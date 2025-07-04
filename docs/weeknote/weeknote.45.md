---
title: "Weeknote #45"
tags: weeknote, planning applications, relational data, submissions
author: Colm Britton
created: 2025/07/04
updated: 2025/07/04
---

_Weeknotes for 23 June - 4 July_

Rattling through more of the planning application submission spec issues this week, helped massively by our development management colleagues clarifying a few things.

Progress has also continued on converting the “human readable” specifications into more declarative formats.

There’s a [changelog](https://github.com/digital-land/planning-application-data-specification/blob/main/CHANGELOG.md) now (which I talked about last [weeknote](/notes/weeknote/weeknote-44)). If you’re curious, it’s the easiest way to see what’s changed and what’s being worked on.

Some highlights I’m particularly happy about:
- ✅ Made the `contact-details` module consistent across all application types ([#294](https://github.com/digital-land/planning-application-data-specification/issues/294))
- 🏘️ Shared a proposal for a reworked `residential-units` module—with example data ([#284](https://github.com/digital-land/planning-application-data-specification/issues/284#issuecomment-3004494887))
- ✂️ Removed an unused module from the ‘consent under TPO’ application. Less to fill in = better for users.

### Why we use a relation-style

Someone asked me this week: _why do we split the data across multiple datasets?_

My first thought: I really wish we’d had more time to work on the data design manual. We’ve got a principle in there, [“structure data using similar principles to relational databases”](https://standards.planning-data.dev/principles/#structure-data-using-similar-principles-to-relational-databases), but it could use a lot more depth.

Here’s what I said in the moment:


> “It’s about avoiding duplication—and making the data easier to maintain, reuse and extend.
> 
> When the same info appears in multiple places, like the name and description of an Article 4 Direction, it’s easy for inconsistencies to creep in. That’s what we want to avoid.
> 
> So each dataset focuses on one distinct kind of thing. For example:
>   * One for the **direction itself** (name, description, legal bits, dates)
>   * One for the **areas** it applies to
> 
> They link together with shared references. That way, we keep each dataset clean and focused, but still able to give the full picture.”

![Diagram showing a good (left) and bad (right) way to structure Article 4 Direction data. The good example links one direction to multiple areas using IDs, avoiding repetition. The bad example repeats the direction info for each area, causing duplication.](/static/images/notes/images/work/explainer-relational-data.png)

### Submission specifications are a different kind of challenge

I’ve been reflecting on how submission specifications are fundamentally different from most of the other specs we’ve done.

Most specs are about describing a thing: a designation, a document, a policy, a legal instrument. They’re designed for publishing known information after the fact.

Submission specs are different. They shape an interaction between a person and the system. They’re part of a conversation: _“Tell us about your site.”_ _“Has development already started?”_ Based on the answer, more is asked for.

That means we’ve had to make different design choices.

Take flag fields, for example. Normally, we avoid them. If you already have the data, you can infer the flag. But that logic doesn’t work when you’re asking the applicant to provide the info in the first place. For example, take the question about "Has the development already started?"

Normally:
* in the specification - `development-start-date`
* inferrable 
	* development has not started if `development-start-date` is empty
	* development has started if date in `development-start-date`

In submission specification(s):
* `has-development-started` field
* if "yes" provided, tell us when (`development-start-date` field)

So in the submission specs, they serve a real purpose.

But to make this distinction clearer, I’ve started renaming these fields. Anywhere we’re asking a direct yes/no question, the field name should reflect that. For example:

I've been mulling over the difference between the submission specifications and the other specifications we've worked on because it leads to different design decisions.

- `development-completed` renamed as `has-development-completed`
- `householder-development` renamed as `is-householder-development`

This should also indicate that not every field in the submission specifications will flow into the planning application and decision specifications. They play different roles.

### Other work bits

- We updated the [specifications page](https://design.planning.data.gov.uk/specifications) to make the language clearer so it’s easier to understand what we mean by working draft, pilot, and candidate status.
- That “timeline” I mentioned a few weeks back? It’s now called a [Roadmap](https://design.planning.data.gov.uk/project/planning-applications/roadmap) (for the planning applications work). Much better name. 

---

🎾 Right, I'm off to Wimbledon now so see you in a week or so 🎾

