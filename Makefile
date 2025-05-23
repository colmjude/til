# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

init: 
	pip install --upgrade pip
	python3 -m pip install -r requirements.txt
	npm install

update-frontend-package:
	rm -rf node_modules/colmjude-frontend
	npm install

update-packages:
	pip install -r requirements.txt
	npm update

copy/css:
	cp ../../colmjude_static_pages/dist/static/stylesheets/homepage1.css dist/static/stylesheets


copy/imgs:
	mkdir -p dist/static/images/notes/images
	cp -r images/* dist/static/images/notes/images

deploy: render deploy/imgs deploy/stylesheet deploy/notes

deploy/notes:
	scripts/deploy.sh dist/notes/ .

deploy/imgs:
	scripts/deploy-images.sh images/ static/images/notes

deploy/stylesheet:
	scripts/deploy.sh dist/static/stylesheets/colmjude-notes.css static/stylesheets

deploy/javascripts:
	scripts/deploy.sh dist/static/javascripts/notes-search.js static/javascripts

deploy/resources:
	scripts/deploy.sh static/resources/ static/resources/

render:
	python3 render.py
	python3 application/redirects.py

recent/notes:
	python3 recent_updates.py

clean:
	rm -r dist/notes

update: copy/imgs render

black:
	black .

black-check:
	black --check .

flake8:
	flake8 .

lint:	black-check flake8

isort:
	isort --profile black .

assets:
	npm run build:stylesheets
	npm run build:javascripts

serve:
	python -m http.server 8000 --bind 127.0.0.1 --directory dist

local: copy/imgs render assets

watch:
	npm run watch

# - means it will be ignored if file doesn't exist.
# See https://stackoverflow.com/questions/8346118/check-if-a-makefile-exists-before-including-it
-include local.mk

remove-db:
	rm -f dumps/notes.db

sqlite-db: remove-db
	python dump.py

commit-sqlite::
	git add dumps/notes.db
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt sqlite db $(shell date +%F)"; git push origin $(BRANCH))
