---
title: "Using flask url_for"
tags: webdev, python, development, til
author: Colm Britton
created: 2023/05/03
updated: 2023/05/03
---

I find myself using the `url_for` function a lot.

However, I only just released you can pass any params you want to it and these will be made available as URL params to the flask route.

For example,

```
<a href="{{ url_for('blueprint.name', expected=param, another=other, param="I want")}}>A link</a>
```

Then I can access them in the route using `request.args`. For example

```
@blueprint.route('/url/<int:expected>')
def route_func(expected)
    arg1 = request.args.get('another')
    ...
```

This works becuase any arguments that don't match a route parameter will be added as a query string. This means if using `url_for` in your python code then you can unpack a dict to add a host of params to the query string.

```
url_for('blueprint.name', **extra_args)
```
