---
title: Hide element from users
author: Colm Britton
tags: html, accessibility, design, frontend
---

Different ways to hide things from various user groups.

From all users, add CSS:

    display:none
    visibility:hidden // some screen readers ignore display: none

To hide visually but still be accessible by screenreaders

    .visually-hidden {
        position: absolute !important;
        width: 1px !important;
        height: 1px !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        clip: rect(0 0 0 0) !important;
        clip-path: inset(50%) !important;
        border: 0 !important;
        white-space: nowrap !important;
    }

Hide from screenreaders, use [aria-hidden attribute](http://www.w3.org/TR/wai-aria/states_and_properties#aria-hidden)

    aria-hidden="true"

E.g.

    <span aria-hidden="true">Here be redundant or extraneous content</span>

Note that this has mixed browser and screen-reader support.

#### Further reading

* John Foliot on [HTML5 Accessibility: aria-hidden and role=”presentation”](http://john.foliot.ca/aria-hidden/)
* Steve Faulkner on [HTML5 Accessibility Chops: hidden and aria-hidden](http://www.paciellogroup.com/blog/2012/05/html5-accessibility-chops-hidden-and-aria-hidden/)
