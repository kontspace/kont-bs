host:=0.0.0.0
port:=8000

debug:
	./manage.py runserver $(host):$(port)

start-uwsgi:
	uwsgi --socket 127.0.0.1:$(port) \
		--chdir $(shell pwd) \
		--wsgi-file Athena/wsgi.py \
		--master \
		--process 4 \
		--daemonize $(shell pwd)/logs/uwsgi.log \
		--pidfile $(shell pwd)/uwsgi.pid  

stop-uwsgi:
	uwsgi --stop uwsgi.pid

reload-uwsgi: 
	uwsgi --reload uwsgi.pid

collectstatic:
	./manage.py collectstatic --noinput

.PHONY: debug \
	collectstatic \
	reload-uwsgi \
	start-uwsgi \
	stop-uwsgi
