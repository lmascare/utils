## Using django Framework 
 * sudo easy_install pip
 * pip install virtualenv
 * install pycharm as a Python Editor

### Ubuntu
 * Review /usr/local/bin/virtualenvwrapper.sh script to setup.
 * Set VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 in .bashrc before
   sourcing the virtualenvwrapper.sh
 * sudo apt install python-django (or python3-django)

### Centos
 * Create a virtual ENV and add django to it
 * mkdir venv ; cd venv # Create virtual envs in a separate area
 * /usr/bin/virtualenv django
 * source django/bin/activate
 * pip install django


### Starting django
 * cd /u/gitwork/utils/django
 * django-admin startproject bookstore
 * cd bookstore
 * ./manage.py migrate (migrates a SQLite3 DB. look in settings.py)
 * ./manage.py runserver 8008 # Run server on port 8008
 * Point your browser to http://127.0.0.1:8008/
 * Note that DEBUG=True for DEV. Not for Production
 * Add GIT in the Version Control Section

### Add an application
 * ./manage.py startapp store
 * 
#### For the admin superuser
 * Update the admin.py
 * ./manage.py createsuperuser
    * username --> admin
    * email --> admin@kellynoah.com
    * password --> <password>
 * login at http://127.0.0.1:8008/admin
 * To enable access from remote browsers
    * On the Linux host run 'firewall-cmd --permanent --add-port=8008/tcp'
 
### Configure the STORE application
 * ./manage.py startapp store
 * In bookstore/settings.py add 'store', to INSTALL_APPS section
 * ./manage.py makemigrations store
 * ./manage.py sqlmigrate store 0001
 * ./manage.py migrate

### To show the state of the migrations
 * ./manage.py showmigrations. The x shows which are done
 * Install django-registration-redux
    - pip install django-registration-redux

### Blog Application
 * django-admin startproject mysite
 * cd mysite ; ./manage.py migrations
 * ./manage.py startapp blog
 * Create the model (models.py)
 * Add module pytz 'pip install pytz' in your virtualenv (in Centos it already exist)
 * Activate the application by adding it to the INSTALLED_APPS section of settings.py for the project
 * Create the schema
   * In the mysite directory, run ./manage.py makemigrations blog
   * **To look at the SQL, run ./manage.py sqlmigrate blog 001**
   * Run ./manage.py migrate to create the schema
 * 
    
#### Querying the DB
 * Interactive shell (for mysite)
    * ./manage.py shell
      * from django.contrib.auth.models import User
      * from blog.models import Post
      * user = User.objects.get(username='admin')
      * Post.objects.create(title='One more post', slug='one-more-post', body='Post body. ', author=user
      * Post.save() # Not needed with the above syntax
      * Post.objects.all() # Retrieves all Posts
      * all_posts = Post.objects.all()
      * Post.objects.filter(publish__year=2017) # Note the 2 __ in publish_year
      * Post.objects.filter(publish__year=2017, author__username='admin')
      * Post.objects.filter(publish__year=2017)\
         .filter(author__username='admin')
      * Post.objects.filter(publish__year=2017)\
         .exclude(title__startswith='Quigley')
      * Post.objects.order_by('title')  # Ascending order is implied
      * Post.objects.order_by('-title') # Descending order with a -
      * post = Post.objects.get(id=1)   # Get the id of the post
      * post.delete()                   # Delete it
      * 
      
      