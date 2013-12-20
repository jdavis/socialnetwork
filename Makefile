default: run

run:
	python manage.py runserver

sync:
	python manage.py syncdb

clean:
	rm db/social_network.sqlite
