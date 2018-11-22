## Django IMDB Application Tutorial

```
# GitHub Requirements
# Create a new repository. Fork the repository
cd /u/gitwork
git clone git@github.com:lmascare/lank.git
git remote add upstream git@github.com:LarryMasc/lank.git

# Create a .gitignore file in /u/gitwork/lank

# Python requirements for Django
/usr/local/bin/python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django
pip install psycopg2

# PostgreSQL setup
# Download and install PostgreSQL. It will create the DB
# Now create a database, user, schema.
# Set search path to the user

psql ast user postgres (Superuser)
create database <dbname>;
create user <user> password '<password>';
grant all privileges on database <dbname> to <user>;
alter role <user> set search_path = "<user>";
revoke create on schema public from PUBLIC;

# Set ~/.pgpass with the following config
hostname:port:database:username:password Perms 0600

# To ensure all DDL objects are created for the <user> in
# the desired schema.
psql -h <hostname> -d <dbname> -U <user>  
create schema <schema_name>

# Django Setup
django-admin startproject config
mv config django
cd django

# In settings.py
import os
import json
DEBUG = False
set ALLOWED_HOSTS = ['*']

with open('/u/gitwork/django/django/config/.secret_key') as f:
    SECRET_KEY = f.read().strip()

with open('/u/gitwork/django/django/config/.db_settings') as f:
    DATABASES = json.load(f)

TIME_ZONE = 'America/New_York'

# .db_settings (perms 400)
{
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "****",
        "USER": "****",
        "PASSWORD": "****",
        "HOST": "127.0.0.1",
        "PORT": "5432"
    }
}

# .secret_key file (perms 400)
******

./manage.py startapp core

# In settings.py, add 'core' as a list element

# Create your table schema in core/models.py

# Defining the schema
./manage.py makemigrations core

# Register the app with admin
# In core/admin.py add
from .models import Movie
admin.site.register(Movie_

# Create the Superuser
./manage.py createsuperuser

```