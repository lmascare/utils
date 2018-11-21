# Compiling, Installing and Configuring Apache2

## Download the following tarballs
 - apache2
 - apr
 - apr-util
 - apr-iconv
 - pcre
 - mod_wsgi

## Compiling

#### [PCRE](https://ftp.pcre.org/pub/pcre)
 - Download tarball
 - ./configure --prefix=/usr/local/pcre
 - make
 - sudo make install

#### [Apache](http://httpd.apache.org/docs/current/install.html)
 - PREFIX should be /usr/local/apache2
  - Extract apr and apr-util to
    - <httpd_source_tree_root>/srclib
    - ensure directory names do NOT have versions
  - apache2
    - ./configure --prefix=/usr/local/apache2 \
    --with-included-apr --with-pcre=/usr/local/pcre
    - make
    - sudo make install

#### [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html)
 - Download [tarball](https://github.com/GrahamDumpleton/mod_wsgi/releases)
 - ./configure ----with-apxs=/usr/local/apache2/bin/apxs \
 --with-python=/usr/local/bin/python3
 - make
 - sudo make install
 - Add the module to Apache installation
    - LoadModule wsgi_module modules/mod_wsgi.so

#### Optional Installation of Apache Portable Runtime
 - apr
    - ./configure --prefix=/usr/local/apr 
 - apr-util
    - ./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr
 - apr-iconv
    - ./configure --prefix=/usr/local/apr-iconv --with-apr=/usr/local/apr


### To Enable mod_wsgi
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/

```text
# wsgi Module
LoadModule wsgi_module modules/mod_wsgi.so

<IfModule wsgi_module>
WSGIScriptAlias / /u/gitwork/django/django/config/wsgi.py
WSGIPythonHome /u/gitwork/django/venv
WSGIPythonPath /u/gitwork/django/django
</IfModule>

WSGIDaemonProcess kellynoah.com processes=2 threads=15 \
python-home=/u/gitwork/django/venv \
python-path=/u/gitwork/django/django

WSGIProcessGroup kellynoah.com

Alias /robots.txt /u/gitwork/django/django/static/robots.txt
Alias /favicon.ico /u/gitwork/django/django/static/favicon.ico

Alias /media/ /u/gitwork/django/django/media/
#Alias /static/ /u/gitwork/django/django/static/
Alias /static/ /u/gitwork/django/venv/lib/python3.6/site-packages/django/contrib/admin/static/

<Directory /u/gitwork/django/django/config>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

<Directory /u/gitwork/django/venv/lib/python3.6/site-packages/django/contrib/admin/static>
Require all granted
</Directory>

<Directory /u/gitwork/django/django>
Require all granted
</Directory>

```