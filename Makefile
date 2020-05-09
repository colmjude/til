init: 
	python3 -m pip install -r requirements.txt


copy/css:
	cp ../../colmjude_static_pages/dist/static/stylesheets/homepage1.css dist/static/stylesheets


deploy:
	scripts/deploy.sh dist/notes/ .


render:
	python3 render.py


clean:
	rm -r dist/notes
