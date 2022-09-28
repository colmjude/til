title: "A simple checklist for images"
tags: webdev, images, development, sustainability
author: Colm Britton
created: 2022/09/28
updated: 2022/09/28
--------------------

Images make up a large portion of a website.

More often than not they are the heaviest (file size is big, takes more data to download) part of a page.

They are one of those things where they are much more complicated than you'd imagine.

I by no means do everything you need to do to handle images, but it is a trade off between what provides the best experience and time.

CSS tricks has a good [list of things to consider when working with images](https://css-tricks.com/images-are-hard/).

I've listed out some of my must dos.

## Alt text and captions

Captions are brief descriptions that provide some context.

Alt text is a description of that the image conveys. Use for informative images. Is alt text necessary for decorative images?

They should be different different. If a caption conveys all the information then maybe the alt text can be null.

Example: image of a graph.

Caption would provide some context. *Confirmed COVID cases in UK in early 2020*

Alt text would explain the graph. *Case surged in March, growing exponentially until it peaked on X*

## Things I do

* Use `<figure>` and `<figcaption>` elements when I have visible text with an image
* Add `alt` text
* use SVGs or dom elements where possible
* Use `loading="lazy"` for all images. Why force a user to load an image they aren't going to see? One of the easiest ways to make your site greener!
* optimise the image. I use [squoosh.app](https://squoosh.app/editor) and follow [Jake's formula](https://jakearchibald.com/2021/serving-sharp-images-to-high-density-screens/) - double the largest size the image will be displayed at (e.g. 700px x 2 = 1400px), then reduce the quality as much as possble (how sharp does it need to be?)

I have a jinja macro I use to make it easier to include all the bits I should include by default.

## Things I'd like to do

* Use `<picture>` element with multiple formats and sizes where appropriate
* host on a CDN - how realistic is this for personal sites?
* because I'm using lazy loading do I need to set the width of each `<img>` in pixels so that it takes up the space in the page even before it loads? So that the page doesn't jolt when it loads
* whats my fallback? If an image fails to load should I have a block colour background or something?

