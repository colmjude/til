---
title: "How to install non-npm node packages"
tags: development, node, packages, reuse
author: Colm Britton
created: 2024/03/29
updated: 2024/03/29
---

If you have a node package you want to include in your project but don't want to publish to NPM you can use [gitpkg.now.sh](https://gitpkg.now.sh/).

On the digital-land team we have a frontend package called digital-land-frontend. We use this pattern to include it in most projects/repos.

I do the same personally with a frontend package (colmjude-frontend).

For it to work you need to create a package dir in the repository. You can do this manually or with build tools. For example, in the digital-land-frontend repo with have a directory called `package`. In this directory you need a `package.json` file to define your package.

For example,
```
{
  "name": "colmjude-frontend",
  ...
```

It is a good idea to have a directory in your `package` dir with the same name you've given your package.

Your package dir should look like:
```
/package
  /name-of-package
    ...
  package.json
  ...
```

All the package stuff you want to be accessible once installed should live in the `/name-of-package` directory.

## How to install it

Now it is set up, you can use it in your projects.

To install it include it in the `package.json` file of the project. For example;

```
  ...
  "dependencies": {
    "colmjude-frontend": "https://gitpkg.now.sh/colmjude/colmjude-frontend/package?main"
  },
```

Then, when you run `npm install` it will be installed in `/node_modules` just like any other package.

## Updating the package

If you edit the original package make sure you bump the version number up. In `package.json` edit this line

```
"version": "0.1.0",
```

Then in your project run `nom update`. 

This should update the package. You can run `npm list` to find out what is installed and the version of each package. If the version number doesn't match the version in your package it hasn't updated correctly. I'm not sure why that happens.

In this case, you can delete the package from `/node_modules` and re-run `npm install`.

I include the following target in my `Makefile` to do this in one command.

```
update-node-package:
	rm -rf node_modules/name-of-package
	npm install
```

And, then run `make update-node-package`.
