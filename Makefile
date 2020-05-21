init: 
	python3 -m pip install -r requirements.txt


copy/css:
	cp ../../colmjude_static_pages/dist/static/stylesheets/homepage1.css dist/static/stylesheets


copy/imgs:
	cp -r images/* dist/static/images/notes/

deploy:
	scripts/deploy.sh dist/notes/ .


deploy/imgs:
	scripts/deploy.sh images/* static/images/notes/.

render:
	python3 render.py


clean:
	rm -r dist/notes
