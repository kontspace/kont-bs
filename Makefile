host:=0.0.0.0
port:=8000

debug:
	./manage.py runserver $(host):$(port)

start-uwsgi:
	. $(shell pwd)/venv/bin/activate && \
	uwsgi --socket $(host):$(port) \
		--chdir $(shell pwd) \
		--wsgi-file Athena/wsgi.py \
		--master \
		--process 4 \
		--daemonize $(shell pwd)/logs/uwsgi.log \
		--pidfile $(shell pwd)/uwsgi.pid  

stop-uwsgi:
	. $(shell pwd)/venv/bin/activate && \
	uwsgi --stop uwsgi.pid

reload-uwsgi: 
	. $(shell pwd)/venv/bin/activate && \
	uwsgi --reload uwsgi.pid

collectstatic:
	. $(shell pwd)/venv/bin/activate && \
	./manage.py collectstatic --noinput

deploy-gunicorn:
	. $(shell pwd)/venv/bin/activate && \
	gunicorn -w 4 Athena.wsgi -b $(host):$(port)

.PHONY: debug \
	collectstatic \
	reload-uwsgi \
	start-uwsgi \
	stop-uwsgi \
	debug-gunicorn	
