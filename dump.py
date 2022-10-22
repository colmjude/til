import json
import sqlite_utils

from config import Config
from application.markdown import initiate_markdown
from note import Notes, note_index


def write_sqlite(notes):
    db = sqlite_utils.Database("tmp/notes.db")
    db["notes"].insert_all(notes)
    db["notes"].enable_fts(["title", "content"])


def add_section(output):
    for n in output:
        n["section"] = "notes"
    return output


def flatten_author(output):
    for n in output:
        n["author"] = n["author"][0]
    return output


def pipeline(output):
    # how do I do a pipeline type process
    output = add_section(output)
    output = flatten_author(output)
    return output


def dump_notes():
    config = Config()
    output = []

    notes = Notes(config.NOTES_ROOT, initiate_markdown(note_index()))

    output = pipeline([notes.notes[note].to_json() for note in notes.notes])

    # with open("notes.json", "w") as f:
    #     json.dump(output, f)

    write_sqlite(output)


if __name__ == "__main__":
    dump_notes()
