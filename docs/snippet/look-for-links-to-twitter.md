title: "Script to look for links to twitter"
tags: webdev, code, gist
author: Colm Britton
--------------------

Recently, I wanted to try out the [BeautifulSoup python library](https://pypi.org/project/beautifulsoup4/).

At work we have an [organisation dataset](https://github.com/digital-land/organisation-dataset/blob/master/collection/organisation.csv) that includes the twitter handle for the organisation. The dataset adds this field by looking at the [wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) entry for a given organisation. If wikidata doesn't have the twitter handle we don't add it to our dataset. There were a lot missing.

So I wrote a quick script to loop over the list of organisations, visit their webpage and search (using BeautifulSoup) for any outbound links to twitter, assuming if they exist it'll point to their twitter account.

If it finds any potential hits I can check them and add them to wikidata (Can you programatically add things to wikidata?).

Here is the script (loaded from a github gist):

<script src="https://gist.github.com/colmjude/7285eec6c9ed7ecd3c2dc04aae1884b7.js"></script>
