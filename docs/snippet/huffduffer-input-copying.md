title: "Huffduffer input copying"
tags: frontend, js
author: Colm Britton
--------------------

[Huffduffer](https://huffduffer.com/colmjude/102092) has a nice little feature that helps a user copy some content. It puts the content in a <code>input</code> element and selects the whole lot when the user clicks on it.

It is an enhancement, done with JS.

An event listener waits for a click, checks if the input has a *readonly* attribute and then selects the whole contents of the input. E.g. 

    this.$module.addEventListener('click', function (ev) {
        var target = ev.target
        if (target.hasAttribute('readonly')) {
            target.focus()
            target.select()
        }
    })
