## Using django Framework
  * sudo easy_install pip
  * pip install virtualenv

  ### Ubuntu
  * Review /usr/local/bin/virtualenvwrapper.sh script to setup.
  * Set VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 in .bashrc before
    sourcing the virtualenvwrapper.sh
  * sudo apt install python-django (or python3-django)

  ### Centos
  * /usr/bin/virtualenv bookstore-django

  * cd /u/gitwork/utils/django
  * django-admin startproject bookstore
  * cd bookstore
  * ./manage.py migrate (migrates a SQLite3 DB. look in settings.py)
  * ./manage.py runserver
  * Point your browser to http://127.0.0.1:8000/

  * Add to GIT

