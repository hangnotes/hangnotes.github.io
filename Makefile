# Makefile for Jekyll Blog Workflow

MICROBLOG_TEMPLATE := _templates/microblog
BLOG_TEMPLATE := _templates/blog

POST_DATE := $(shell date +%Y-%m-%d)
POST_TIME := $(shell date +%Y-%m-%d\ %T\ %z)

POST_TITLE := $(shell openssl rand 100000 | shasum | cut -c1-8)
BLOG_TITLE := $(title)

POST_FILE := _microblog/$(POST_DATE)-$(POST_TITLE).md
BLOG_FILE := _posts/$(POST_DATE)-$(BLOG_TITLE).md

.PHONY: post blog serve publish install

# Create a new blog post: make post title="My New Title" tags="tag1,tag2"
post:
	@python3 scripts/new_post.py

# Legacy blog creator target: make blog title=my-post-slug
blog:
	@cat $(BLOG_TEMPLATE) | sed "s/%CURRENT_DATE%/$(POST_TIME)/g" > ${BLOG_FILE}
	@echo "Created ${BLOG_FILE}"

# Start local server preview
serve s:
	JEKYLL_ENV=production bundle exec jekyll serve

# Publish changes to GitHub Pages: make publish [msg="commit message"]
publish:
	git add .
	git commit -m "$(if $(msg),$(msg),Publish new post)"
	git push origin main

install:
	bundle install
