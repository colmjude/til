init: 
	python3 -m pip install -r requirements.txt


copy/css:
	cp ../../colmjude_static_pages/dist/static/stylesheets/homepage1.css dist/static/stylesheets


copy/imgs:
	cp -r images/* dist/static/images/notes/

deploy: render deploy/imgs
	scripts/deploy.sh dist/notes/ .


deploy/imgs:
	scripts/deploy.sh images/ static/images/notes/

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

serve:
	python -m http.server 8000 --bind 127.0.0.1 --directory dist

include local.mk
