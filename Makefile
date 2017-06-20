host:=0.0.0.0
port:=8005

debug:
	./manage.py runserver $(host):$(port)

collectstatic:
	. $(shell pwd)/venv/bin/activate && \
	./manage.py collectstatic --noinput

start-uwsgi:
	. $(shell pwd)/venv/bin/activate && \
	uwsgi --http $(host):$(port) \
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


.PHONY: debug \
	collectstatic \
	reload-uwsgi \
	start-uwsgi \
	stop-uwsgi
