def generate_tag_url(tag):
    if tag == "weeknote":
        return "/notes/weeknote"
    else:
        return "/notes/tag/" + tag.lower().replace(" ", "-")
