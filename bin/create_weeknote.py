import os
import sys

from create_til import base_dir, prepare_template, save_markdown_file

weeknote_template = """
## Targets

## What have I done

### Career / profile

### GWG

### Other

## What have I read

## What have I written

## What have I made

## What have I learnt

## Things I should do/learn about
"""

def flatten_date(d):
    return d.replace("-", "")


def create_weeknote(d):
    til_dir = f"{base_dir}weeknote/"

    if not os.path.isdir(til_dir):
        os.mkdir(til_dir)

    weeknote_title = f"weeknote.{flatten_date(d)}.md"
    til_path = os.path.join(til_dir, weeknote_title)
    if os.path.isfile(til_path):
        print(f"ERROR: {til_path} already exists")
    else:
        content = prepare_template(weeknote_title)
        content = content + weeknote_template
        save_markdown_file(til_path, content)


if __name__ == "__main__":
    args_provided = sys.argv[1:]
    if len(args_provided):
        create_weeknote(args_provided[0])
    else:
        print("No title provided")