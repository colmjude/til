import markdown
from markdown.extensions.wikilinks import WikiLinkExtension


def initiate_markdown(idx, base_url="/notes/"):
    def wikilink_builder(label, base, end):
        # this only does top level notes
        # e.g. /notes/<note slug>.html
        # need to do something more comprehensive
        # notes = Notes(config.NOTES_ROOT)
        # url = f"{base}{title_to_slug(label)}{end}"
        return idx.get(label) + end

    return markdown.Markdown(
        extensions=[
            "meta",
            WikiLinkExtension(
                base_url=base_url, end_url=".html", build_url=wikilink_builder
            ),
        ]
    )
