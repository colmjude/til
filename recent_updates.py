import argparse
from datetime import datetime, timedelta

from application.markdown import initiate_markdown
from note import Notes, note_index


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Please use yyyy-mm-dd.")


def get_default_from_date():
    return (datetime.now() - timedelta(weeks=1)).strftime("%Y-%m-%d")


def recent_updates():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from",
        dest="from_date",
        metavar="YYYY-MM-DD",
        type=parse_date,
        default=get_default_from_date(),
        help="Date to go back to (format: yyyy-mm-dd)",
    )
    args = parser.parse_args()

    notes = Notes("docs/", initiate_markdown(note_index()))

    # Iterate over the notes
    print("")
    print("Recently updated notes")
    print("======================")
    print("")

    for note in notes.notes.values():
        if not note.draft:
            if "updated" in note.frontmatter.keys():
                updated_date_str = note.frontmatter["updated"]
                # Check if the updated_date is within the last week
                updated_date = datetime.strptime(updated_date_str, "%Y/%m/%d")
                if updated_date >= args.from_date:
                    # Print the note name and URL
                    print(f"[{note.title}](/notes/{note.parent_category}/{note.slug})")


if __name__ == "__main__":
    recent_updates()
