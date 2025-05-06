import json
import sqlite_utils
from typing import List

from config import Config
from application.markdown import initiate_markdown
from application.models import Note
from note import Notes, note_index


def write_sqlite(notes: List[Note]):
    db = sqlite_utils.Database("dumps/notes.db")

    if "notes" in db.table_names():
        db["notes"].drop()

    # Use Pydantic's built-in schema generation
    schema = Note.model_json_schema()
    db_schema = {
        field: type(props.get("type", str))
        for field, props in schema["properties"].items()
    }

    db["notes"].create(db_schema, pk="slug")
    notes_dict = [note.model_dump() for note in notes]
    db["notes"].insert_all(notes_dict)
    db["notes"].enable_fts(["title", "content"])


def add_section(output):
    for n in output:
        if n.get("section") is "":
            n["section"] = "notes"
    return output


def flatten_author(output):
    for n in output:
        if isinstance(n["author"], list):
            n["author"] = n["author"][0]
    return output


def pipeline(output):
    # how do I do a pipeline type process
    output = add_section(output)
    output = flatten_author(output)
    return [Note(**note) for note in output]


def dump_notes():
    config = Config()
    # output = []

    notes = Notes(config.NOTES_ROOT, initiate_markdown(note_index()))
    raw_notes = [notes.notes[note].to_json() for note in notes.notes]
    validated_notes = pipeline(raw_notes)

    # output = pipeline([notes.notes[note].to_json() for note in notes.notes])

    # with open("notes.json", "w") as f:
    #     json.dump(output, f)

    write_sqlite(validated_notes)


if __name__ == "__main__":
    dump_notes()
