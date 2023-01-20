# TIL and snippets

A little python tool to collect my TIL notes and snippets.

### Use

Best to work in a virtual environment.

Install dependencies

    $ pip install -r requirements.txt

Create a note

    $ python bin/create_til.py <<title of note>>

### Custom Markdown

WikiLinks are enabled. But currently only work for referencing top-level notes

    [[WikiLink]] - becomes /notes/wikilink.html

### Embed tweets

To use the markdown extension set the access credentials in `.env`.

```
TW_API_KEY=<key>
TW_API_KEY_SECRET=<key-secret>
TW_ACCESS_TOKEN=<token>
TW_ACCESS_TOKEN_SECRET=<token-secret>
```

And use it using the following format

```
{{:twitter https://twitter.com/ColmBritton/status/1583455055088271360}}
```

### To deploy

Firstly set up `.env` file with credentials needed to ftp into webhost.

```
WEBHOST=<webhost>
WEBPORT=<webport>
PATHTODIR=<path to public_html dir>
```
