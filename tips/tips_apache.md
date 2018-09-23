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
