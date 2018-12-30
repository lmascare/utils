## Django Application for LANK Enterprises

#### Python requirements for Django
```
/usr/local/bin/python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django
pip install psycopg2
pip install psycopg2-binary
```

#### Django Setup
```
cd /u/gitwork/lank
source venv/bin/activate
django-admin startproject config
mv config django
cd django
```

#### Update settings.py
 * DATABASES
 * secret_key
 * ALLOWED_HOSTS
 * import json

#### Static files are not served by Django Webserver. Use Apache instead
#### Enable _core_ application
```
./manage.py migrate
./manage.py createsuperuser
./manage.py startapp core

```

####[Custom User](https://wsvincent.com/django-allauth-tutorial-custom-user-model/)
#####Decide _BEFORE_ project is created
```
./manage.py startapp users
# Add to settings.py
    'users' to INSTALLED_APPS
    AUTH_USER_MODEL = 'users.CustomUser'
./manage.py createsuperuser
```

####Filters
```markdown
pip install django-filter
# Add to settings.py
    'django_filters' to INSTALLED_APPS
```