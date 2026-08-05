#!/usr/bin/env python3
import sys
import os
import datetime
import re

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def main():
    title = os.environ.get("title") or (sys.argv[1] if len(sys.argv) > 1 else None)
    tags_str = os.environ.get("tags") or (sys.argv[2] if len(sys.argv) > 2 else "")
    category = os.environ.get("category") or "随笔"

    if not title:
        title = input("Enter post title: ").strip()
        if not title:
            print("Error: Post title is required.")
            sys.exit(1)

    slug = os.environ.get("slug")
    if not slug:
        slug = slugify(title)
        if not slug:
            slug = "post-" + datetime.datetime.now().strftime("%H%M%S")

    today = datetime.datetime.now().astimezone()
    date_str = today.strftime("%Y-%m-%d")
    datetime_str = today.strftime("%Y-%m-%d %H:%M:%S %z")

    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    tags_formatted = "[" + ", ".join(tags) + "]" if tags else "[]"

    filename = f"_posts/{date_str}-{slug}.md"
    filepath = os.path.join(os.getcwd(), filename)

    content = f"""---
layout: post
title: "{title}"
date: {datetime_str}
category: {category}
tags: {tags_formatted}
comments: true
---

Write your article content here...
"""

    if os.path.exists(filepath):
        print(f"File already exists: {filename}")
        sys.exit(1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created new post draft: {filename}")

if __name__ == "__main__":
    main()
