## Django IMDB Application Tutorial

```
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
set ALLOWED_HOSTS = ['*']
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