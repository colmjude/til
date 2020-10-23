title: "insert-hidden-text-js"
tags: accessibility, js, web-dev
author: Colm Britton
--------------------

When progressively enhancing elements you might have the need to add some visually hidden text (text that is not displayed but that will be read by a screen reader).

An example would be in a link. It is quite common to see a link with the text **edit**. The position of the link/button on the page helps users using the page visually to associate the action with something. E.g. if it is next to your email address you can safely assume click on it will let you edit your email. However if you can't take in that visual relationship you might need another way to understand clicking that particular edit button will let you edit the email address.

That is where you can add visually hidden text.

Easy to have a class you can use when writing your HTML.

    <button>Edit<span class="visually-hidden"> your email address</span></button>

There will be times you will be creating this with js. Progressive enhancement.

You will need to create a text node rather than use the `textContent` attribute of any elemetn you create.

Sample code

    var _link = document.createElement('a')
    _link.setAttribute('href', params.linkHref)

    var a11yText = document.createElement('span')
    a11yText.classList.add('govuk-visually-hidden')
    a11yText.textContent = 'highlight row '
    _link.append(a11yText)

    var _linkContent = document.createTextNode('#' + params.linkIdx)
    _link.append(_linkContent)
    _link.addEventListener('click', boundLinkToRowHandler)

    cell.append(_link)
