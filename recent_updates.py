from datetime import datetime, timedelta

from application.markdown import initiate_markdown
from note import Notes, note_index


def recent_updates():
    notes = Notes("docs/", initiate_markdown(note_index()))

    # Calculate the date one week ago
    one_week_ago = datetime.now() - timedelta(weeks=1)

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
                if updated_date >= one_week_ago:
                    # Print the note name and URL
                    print(f"[{note.title}](/notes/{note.parent_category}/{note.slug})")


if __name__ == "__main__":
    recent_updates()
