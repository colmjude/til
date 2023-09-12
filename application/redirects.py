#!/usr/bin/env python3

import os
import frontmatter


def generate_redirects_htaccess(redirects=[], htaccess_file=".htaccess-test"):
    # redirects = [
    #     ("/old-page.html", "http://www.example.com/new-page.html"),
    #     ("/another-old-page.html", "http://www.example.com/another-new-page.html"),
    #     # Add more redirects as needed
    # ] + redirects

    lines = [
        "Redirect 301 {} {}".format(old_url, new_url) for old_url, new_url in redirects
    ]
    htaccess_content = "\n".join(lines)

    with open(htaccess_file, "w") as htaccess_file:
        rewrite_on = """
<IfModule mod_rewrite.c>
RewriteEngine On
</IfModule>

"""
        htaccess_file.write(rewrite_on)
        htaccess_file.write(htaccess_content)


def weeknote_redirects():
    redirects = []
    weeknote_dir = "docs/weeknote/"
    weeknote_list = os.listdir(weeknote_dir)

    for weeknote_file in weeknote_list:
        file_path = os.path.join(weeknote_dir, weeknote_file)
        weeknote = frontmatter.load(file_path)
        if "redirect" in weeknote.metadata:
            for redirect_entry in weeknote.metadata["redirect"]:
                slug = weeknote_file.strip(".md").replace(".", "-")
                new_url = f"https://colmjude.com/notes/weeknote/{slug}/"
                redirects.append((redirect_entry["url"], new_url))

    generate_redirects_htaccess(redirects, "dist/notes/weeknote/.htaccess")


weeknote_redirects()
# generate_redirects_htaccess()
