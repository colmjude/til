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

### To deploy

Firstly set up `.env` file with credentials needed to ftp into webhost.

```
WEBHOST=<webhost>
WEBPORT=<webport>
PATHTODIR=<path to public_html dir>
```
