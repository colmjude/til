title: JS Snippets
tags: webdev, js, snippets
author: Colm Britton
created: 2023/02/01
updated: 2023/02/01
--------------------

TIL you can use logic, such as a ternary operator, in ES6 template literals (or back tick strings).

For example,

```
`${result['color 5'] ? 'color 5 exists!' : 'color 5 does not exist!'}`
```

Which is very handy if you are passing data to a template like string and some of the data is optional - in this case you might not want anything to show up or you can provide a sensible default. For example on gwg,

```
`<h4>${gift.name}</h4>
<div class="gift-description">
  <p>${gift.description ? gift.description : ''}</p>
</div>`
```

The [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) documentation mentions you can embed any expression in template literals. So things like functions and even IIFEs. 
