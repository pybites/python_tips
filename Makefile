.PHONY: venv
venv:
	python3.9 -m venv venv

.PHONY: install
install:
	. venv/bin/activate && pip install -r requirements.txt

.PHONY: secret
secret:
	. venv/bin/activate && python -c "import string, random; print('export SECRET_KEY=' + ''.join(random.sample(string.ascii_lowercase + string.digits, 20)))" >> venv/bin/activate

.PHONY: debug
debug:
	. venv/bin/activate && echo "export DEBUG=True" >> venv/bin/activate

.PHONY: migrate
migrate:
	. venv/bin/activate && python manage.py migrate

.PHONY: su
su:
	. venv/bin/activate && echo "from django.contrib.auth.models import User; User.objects.create_superuser('pybites', 'pybites@example.com', 'changeme')" | python manage.py shell

.PHONY: tips
tips:
	. venv/bin/activate && python manage.py sync_tips

.PHONY: setup
setup: venv install secret debug migrate su tips

.PHONY: run
run:
	. venv/bin/activate && python manage.py runserver
