title: Embedding tweets in markdown notes
tags: webdev, development, twitter, markdown, python
author: Colm Britton
created: 2023/01/20
updated: 2023/01/20
--------------------

I wanted to embed a tweet in a note. I thought, everyone does this so it must be easy.

Now it is easy if you want to manually go to twitter each time you want to embed a tweet and copy the embed code.

But I wanted to be able to use the URL so that it would be marginally quicker (and easier to read in the markdown).

I looked for an existing python markdown extension but couldn't find one. I'm sure there must be one somewhere but finding it was beyond me.

So, instead, I wrote my own 🫣

Firstly, I used this [blog post about embedding a tweet in a flask blog](https://ezzeddinabdullah.com/post/embed-tweet-blog-flask-headless-cms/) as inspiration.

Task one was setting up a [Twitter developer account](https://developer.twitter.com/en) - to get credentials for accessing twitter. It's easy and free. You need to create a project, an app and then generate an access token to go with the API key.

I used the [tweepy](https://docs.tweepy.org/) library which has a [get_oembed](https://docs.tweepy.org/en/stable/api.html#post-retrieve-and-engage-with-tweets) function. This function takes a twitter url and returns the HTML for embedding the tweet.

I then created a markdown extension that would match a pattern like

```
{{:twitter <twitter-url>}}
```

For example
```
{{:twitter https://twitter.com/ColmBritton/status/1583455055088271360}}
```

Which should embed one of my tweets...

{{:twitter https://twitter.com/ColmBritton/status/1583455055088271360}}

### Useful links

* [markdown extensions](https://python-markdown.github.io/extensions/api/)
* [twitter-to-sqlite library](https://github.com/dogsheep/twitter-to-sqlite)
* [a few ideas for markdown extensions](https://alexwlchan.net/2017/extensions-in-python-markdown/)
* [how to use `markdown.inlinepatterns.Pattern`](https://snyk.io/advisor/python/Markdown/functions/markdown.inlinepatterns.Pattern)
* [tweepy](https://docs.tweepy.org/)
* [twitter's developer portal](https://developer.twitter.com/)
