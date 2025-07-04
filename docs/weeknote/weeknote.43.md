---
title: "Weeknote #43"
tags: weeknote, declarative model, planning applications, dates
author: Colm Britton
created: 2025/06/01
updated: 2025/06/08
---

_This weeknote covers 26 May - 6 June_

The last two weeks have been a bit of a blur with some real progress made, but plenty still circling.

### Declarative modelling

In my last [weeknote](/notes/weeknote/weeknote-42/), I mentioned starting to write up what a declarative model might look like for the planning applications work. This fortnight, I fleshed it out and published a first cut of that thinking:

	•	[What is a declarative model?](https://github.com/digital-land/planning-application-data-specification/blob/main/docs/declarative-model.md)
	•	[Module interface](https://github.com/digital-land/planning-application-data-specification/blob/main/docs/module.md)
	•	[Field interface](https://github.com/digital-land/planning-application-data-specification/blob/main/docs/fields.md)
	•	[Planning requirements](https://github.com/digital-land/planning-application-data-specification/blob/main/docs/planning-requirements.md) – we’re not tackling these just yet, but after the conversation with Camden, I wanted to get something down to frame future work.

This work is foundational. If we want the specifications to be understandable, adoptable, and scalable, we need to define clear interfaces and shared expectations. And, in my opinion, that means shifting to a more declarative model.

### Planning applications

I published the [draft timeline](https://design.planning.data.gov.uk/advisory-group/timeline) for the planning application spec work. It's a list of key activities and upcoming deliverables. So, we should actually call it a roadmap. I linked to it from the advisory group page.

That sparked a wider conversation about the purpose and structure of those pages. Originally, they were just for updates and useful links. But the work has outgrown that. The page now acts more like a central hub for everything planning-application-related.

We’re starting to explore how to redesign this content around clearer units of work. That likely means structuring things around:

	•	projects (like the planning application spec work)
	•	considerations (like design codes, or validation rules)
	•	datasets (like conditions or site allocations)

This would also give us room to support other streams properly. For example, local plans, which could really do with a page of its own.

On the call for feedback: we received it across email threads, shared docs, and GitHub comments. Kieran kindly [collated it all into one place](https://docs.google.com/spreadsheets/d/10QprqRCo8Ss_Hpx-XkXpVHmVGewiTzWbVITEz9vXvhw/edit?usp=sharing), and I spent a fair chunk of time reviewing and responding.

So far, that’s meant:

	•	63 items resolved
	•	[93 new GitHub issues raised](https://github.com/digital-land/planning-application-data-specification/issues)

### Dates (again)

Dates continue to be tricky. I posted [a write-up of the recent “effective-date” discussion](https://github.com/digital-land/data-standards-backlog/discussions/149#discussioncomment-13351739) I had with Camden.

That example made a strong case for needing a fourth kind of date. To represent the policy lifecycle, we seem to need:

	•	`entry-date` - when the data was created
	•	`start-date` - when the policy starts to carry weight (even in draft)
	•	`end-date` - when it’s no longer in force
	•	`effective-date` - when it officially comes into effect (e.g. adoption)

This is just one example but there is a broader question to answer (or at least its bothering me) about understanding the different roles dates play. Broadly, I've seen

	•	system dates - used internally to track versions
	•	significant dates – affect the meaning or legal status of the thing
	•	process dates – document how something came to be (like a log or audit trail)
	•	and maybe other. We are still exploring this space.

Camden also shared a great example about Article 4 directions. Where a direction can be agreed, made public and still not be “in play.” In this case, our current model seems to hold up, but it’s a good test case for stress-testing the definitions.

That’s it for now. More soon.
