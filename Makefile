default: run

run:
	python manage.py runserver 192.168.1.142:8000

sync:
	python manage.py syncdb

clean:
	rm db/social_network.sqlite
