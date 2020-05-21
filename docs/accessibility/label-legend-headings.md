title: "Headings, labels and legends"
tags: accessibility, design, frontend
author: Colm Britton
--------------------

You can now safely use `h1` elements inside a `legend` element or add a `label` element inside a `h1` element.

[Updated HTML spec](https://github.com/whatwg/html/pull/5090).

This is good when you only have one thing per page, such as, asking for post code. Previously we might've had the `h1` and the `label` have the same content but with the `label` visually hidden; fine when experiencing page visually but not so much if via a screen reader, e.g a heading and label with the text "What is your post code?" will be read twice.

[Longer explanation on GOV.UK design system](https://design-system.service.gov.uk/get-started/labels-legends-headings/)

Now fine

    <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
      <h1 class="govuk-fieldset__heading">
        govuk-fieldset__legend--l
      </h1>
    </legend>
