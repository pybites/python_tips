# PyBites Tips API

## Part of the 100 Days of web with Python Talk Python Course

Here are the instructions to set this API up locally.

If you want to automate below in one step, you can use the included `Makefile`. In that case you can just run `make setup && make run` and you should be good to go.

To do this setup manually go through these steps:

1. Make a virtual environment: `python -m venv venv`.

2. Activate the virtual environment: `source venv/bin/activate`.

3. Install the (base) requirements: `pip install -r requirements.txt`.

4. Set `SECRET_KEY` and `DEBUG` in the `venv/bin/activate` script and run it again so these variables are available.

5. Run the migrations: `python manage.py migrate`.

6. Create a pybites superuser with password 'changeme':

```
echo "from django.contrib.auth.models import User; User.objects.create_superuser('pybites', 'pybites@example.com', 'changeme')" | python manage.py shell
```

7. Import the tips data: `python manage.py sync_tips`.

8. Run the webserver: `python manage.py runserver`.

---

Browse to [http://localhost:8000/api/](http://localhost:8000/api/) - enjoy!

---

This API was initially linked to: [Building a Python Tips API with Django REST Framework and Deploying it to Digital Ocean](https://pybit.es/django-rest-tips-api-digital-ocean.html) - leaving this here just in case.
