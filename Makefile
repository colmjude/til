init: 
	python3 -m pip install -r requirements.txt
	npm install

update-packages:
	pip install -r requirements.txt
	npm update

copy/css:
	cp ../../colmjude_static_pages/dist/static/stylesheets/homepage1.css dist/static/stylesheets


copy/imgs:
	cp -r images/* dist/static/images/notes/

deploy: render deploy/imgs deploy/stylesheet
	scripts/deploy.sh dist/notes/ .

deploy/imgs:
	scripts/deploy.sh images/ static/images/notes/

deploy/stylesheet:
	scripts/deploy.sh dist/static/stylesheets/colmjude-notes.css static/stylesheets

render:
	python3 render.py


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

serve:
	python -m http.server 8000 --bind 127.0.0.1 --directory dist

local: render assets

include local.mk
