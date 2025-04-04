import datetime


def generate_tag_url(tag):
    if tag == "weeknote":
        return "/notes/weeknote"
    else:
        return "/notes/tag/" + tag.lower().replace(" ", "-")


def format_timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
