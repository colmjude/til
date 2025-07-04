---
title: "Weeknote #44"
tags: weeknote, planning applications, declarative model, tooling, extract, ai
author: Colm Britton
created: 2025/06/13
updated: 2025/07/03
---

_This weeknote covers 9 June - 20 June_

A lot of progress this fortnight, mostly continuing the detailed work on the planning application submission specifications, and what follows.

### Submission specification(s): still going strong

I spent most of the week working through issues in the planning application submission specifications. Some of it was technical cleanup, some of it more strategic.

One small but satisfying moment: we finally removed the `fax-number` field from the contact details module. I'm pleased about that.

### Tracking changes

I’ve set up [a changelog for the planning application work](https://github.com/digital-land/planning-application-data-specification/blob/main/CHANGELOG.md). It’s not essential for this phase but it will be.

Once specifications are mandated, we’ll need a clear, reliable change history. Doing it now lets us test what’s actually useful to people. What belongs in a changelog? What doesn’t? Etc.

It also helps demonstrate the scale of the work. When everything’s in flight, a running changelog is a good way to show what’s already been done.

I used [git-chglog](https://github.com/git-chglog/git-chglog), which was refreshingly easy to get going. [Steps are documented in a note](/notes/development/an-automated-changelog).

### A declaractive householder specification

I completed the declarative version of the householder application spec, including:
	•	the full application definition
	•	all applicable modules
	•	reusable components
	•	all individual fields

Having a full, worked example really helped validate the approach.

Some parts are feeling solid. For example, defining a field that points to a reusable component:

```yaml
datatype: object  
component: contact-details
```

That pattern’s proving clean and easy to follow.

Other bits still need thinking, especially conditions like this:

```
fields:
  - field: an-example-field
    applies-if:
      - application-type:
        - in: ["full", "outline"]
```

Working with real cases makes a big difference.

I’ve also started adding [module-level data examples](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/example). The idea is to eventually compile these into complete payloads with a bit of tooling.


### Tooling

Now that we’re moving toward a more declarative approach, we can start validating the specifications in new ways.

So I’ve added some lightweight tooling to check basic integrity across applications, modules, components, and fields. It’s not fancy, but it’s enough to catch bad references and structure errors before they become problems.

On a related note, I’ve added [a list of modules with active issues](https://github.com/digital-land/planning-application-data-specification/blob/main/issue-tracking/index.md). This should save us from repeatedly asking “which ones still need work?” It’s a live tracker: as issues are resolved, modules drop off the list.

### Applications and decisions

We’re revisiting the planning applications and decisions space. Drew, Elliot, and I had an earlier whiteboard session, and I’ve now drafted a deliberately limited data model for decisions. I’ve shared [a write-up in the GitHub discussion](https://github.com/digital-land/data-standards-backlog/discussions/25#discussioncomment-13530686).

Unfortunately, due to changes in our Mural accounts, I can’t currently share the original board. Working on it.

In the meantime, we’re kicking off a research piece focused on decisions. With submissions, we worked from an existing set of requirements (the application forms). Those defined the shape of the work.

With decisions, we’re flipping it:
	•	start small
	•	only include what we’re confident about
	•	use the community and user research to surface what’s really needed

It’s a different approach, but a necessary one. Lots of people want access to this data so it's important we figure out what will actually be useful.

### Other updates

	•	more [planning condition data is now on the platform](https://www.planning.data.gov.uk/dataset/planning-condition), thanks to another batch from Doncaster
	•	I tweaked the [listed building dataset specification](https://digital-land.github.io/specification/specification/listed-building/) after we reviewed HMLR’s local land charge data. We’ve added `uprns` to capture all properties affected, and reintroduced a `description` field. I this case, essential for explaining whether the dataset refers to curtilage, property boundary, or something else.

---

## In other news 

The Prime Minister announced Extract, a new AI tool to help councils digitise old planning documents:
👉 [i.AI plans rollout of Extract AI tool for councils – UKAuthority](https://www.ukauthority.com/articles/iai-plans-roll-out-of-extract-ai-tool-for-councils)

Extract should make it much easier for local authorities to generate data that fits our specifications. That means more data, faster, and that’s key to improving services and speeding up planning decisions.

The team behind Extract said our specifications made their lives easier. They didn’t have to invent structure, they could just plug into what was already there.

That was encouraging to hear. Because that’s the whole point.
We’re doing the work to define usable, consistent specifications so others don’t have to.
Then, they can focus on their part of the puzzle; digitising, interpreting, integrating and building services knowing the structure’s already in place.

And that’s how we start to unlock better data, build better services and make better decisions.
