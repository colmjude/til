---
title: "An automated changelog"
tags: development, til, git, commits, changelog
author: Colm Britton
created: 2025/06/26
updated: 2025/06/28
---

 Imagine spending precious development time compiling a list of changes instead of working on the product.

That's the exact situation I found myself in with the planning applications data specification(s) work. 

By adopting a structured changelog workflow, you'll save hours and have ready made release notes available to all your users.

I'll explain how.

### Be consistent with your commit messages

First, its important to adopt a standard approach to your commit messages. The industry standard seems to be [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so I'd just go with that. Conventional commits is a "specification for adding human and machine readable meaning to commit messages" - essentially, you add a little structure and discipline to your commit message, and then automation tools can do stuff with them.

Talking of automation tools, one is [git-chglog](https://github.com/git-chglog/git-chglog).
### Install and use

What's cool about git-chglog is that it lets you set what types of commits it should include and group together in the log. It works on git tags and you have control of the layout of the changelog.

So how to use it?

Install it with brew (macos) and initalise in your repo
```
# Install the changelog generator  
brew install git-chglog

# Initialise your config  
git-chglog --init
```

This set creates two files, both in the `.chglog` directory. They are
* **config.yml** - this is where you set 
* **CHANGELOG.tmp.md** - this is the template for the changelog (in GO)

### Design your categories

You get to decide what categories of commits you want to include in the changelog. For example, a few common ones are:
* Features - "feat: this is a new feature"
* Bugs- "bug: this was a bug fix"

Once you decide on what the groupings are, include them in the config file (`.chglog/config.yml`). 

I'm particularly interesting in logging changes to the specifications (its the main thing we are working and changing regularly) and any changes to the applications (ultimately these are the entry point for people so important to capture any changes) so my set up looks like this
```
options:
  commits:
    filters:
      Type:
        - spec
        - app
        - tool
        - fix
        - docs
        - req
  commit_groups:
    title_maps:
      spec: "𝌭 Model changes"
      app: "👷‍♀️ Application changes"
      tool: "⚒️ Tooling"
      fix:  "🐛 Bug Fixes"
      docs: "📚 Documentation"
      req: "📄 Planning requirement"
```

But you can decide on whatever groupings you want. Just make sure you follow the right commit convention. For example:
```
spec: new field X added Y module
```

### Tag and release

You generate the changelog with
```
git-chglog -o CHANGELOG.md
```
where `-o` lets you set the output file

And just like that, you’re generating changelogs

But...

You'll probably what to phase your work into releases or the equivalent.

The easiest way to do that is to use git tags.

For example, create a new tag for the last group on work you did with
```
git tag -a v1.2.0 -m "Release v1.2.0 — Added a brilliant new feature"
```

Now, generate the changelog again
```
git-chglog -o CHANGELOG.md
```

And it'll group the changes made since the last git tag you created.

---

Hope that helps.

See it live in action on our GitHub repo: [planning application data specifications](https://github.com/digital-land/planning-application-data-specification/blob/main/CHANGELOG.md)


---
## Tips

**Include link to the commit**
You can include a link to the commit. For example
> rename contact to contact-reference (commit [48959fc](https://github.com/digital-land/planning-application-data-specification/commit/48959fca0f2f498a8ea293a8e20c378081c44194))

by updating the template. Find the line `* {{ .Subject }}` and replace with 
```
* {{ .Subject }} (commit [{{ .Hash.Short }}]({{ $.Info.RepositoryURL }}/commit/{{ .Hash.Long }}))
```
