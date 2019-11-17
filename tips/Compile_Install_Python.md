## Steps to Download, Compile and Install Python

### Start by making sure your system is up-to-date:
* yum update

### Compilers and related tools:
* yum groupinstall -y "development tools"

### Libraries needed during compilation to enable all features of Python:
* yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel \
  readline-devel tk-devel gdbm-devel \
  db4-devel libpcap-devel xz-devel expat-devel

### If you are on a clean "minimal" install of CentOS you also need the wget tool:
* yum install -y wget

## Python 2.7.14:
* wget http://python.org/ftp/python/2.7.14/Python-2.7.14.tar.xz
* tar xf Python-2.7.14.tar.xz
* cd Python-2.7.14
* ./configure --prefix=/usr/local/python2.7.14 --enable-unicode=ucs4 --enable-shared \
  -enable-optimizations LDFLAGS="-Wl,-rpath /usr/local/lib"
* make && make altinstall
 
## Python 3.6.3:
* wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
* tar xf Python-3.6.3.tar.xz
* cd Python-3.6.3
* ./configure --prefix=/usr/local/python_3.6.3 --enable-shared \
  -enable-optimizations LDFLAGS="-Wl,-rpath /usr/local/lib"
* make && make altinstall

## Python 3.7.3
* wget http://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
* tar xfz ../Downloads/Python-3.7.3.tgz
* cd Python-3.7.3
* CentOS needs 
    * yum install libffi-devel
    * yum install zlib-devel
* Ubuntu needs
    * sudo apt-get install libffi-dev
    * sudo apt-get install zlib1g-dev
    * sudo apt-get install libexpat1-dev
* ./configure --prefix=/usr/local/python_3.7.3 \
    --disable-shared \
     --enable-optimizations \
     --with-lto \
     --with-pydebug
     
```From Stackoverflow```
* ./configure --prefix=/usr/local/python3.7.3 \
  --enable-loadable-sqlite-extensions \
  --enable-shared \
  --with-lto \
  --enable-optimizations \
  --with-system-expat \
  --with-system-ffi \
  --enable-ipv6 --with-threads --with-pydebug --disable-rpath

* 23-June-2019 Compiled with following options on Ubuntu
./configure --prefix=/usr/local/python_3.7.3 \
    --enable-loadable-sqlite-extensions   
    --with-system-ffi

### Strip the Python 2.7 binary:
* strip /usr/local/lib/libpython2.7.so.1.0

### Strip the Python 3.6 binary:
* strip /usr/local/lib/libpython3.6m.so.1.0

### First get the script:
* wget https://bootstrap.pypa.io/get-pip.py
 
### Then execute it using Python 2.7 
### Python 3.6 has pip3 by default
* python2.7 get-pip.py

 
# With pip installed you can now do things like this:
* pip2.7 install [packagename]
* pip2.7 install --upgrade [packagename]
* pip2.7 uninstall [packagename]
* pip freeze > requirements.txt
* pip install -r requirements.txt
* pip install --upgrade -r requirements.txt