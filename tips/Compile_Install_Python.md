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
* ./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared \
  LDFLAGS="-Wl,-rpath /usr/local/lib"
* make && make altinstall
 
## Python 3.6.3:
* wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
* tar xf Python-3.6.3.tar.xz
* cd Python-3.6.3
* ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
* make && make altinstall


### Strip the Python 2.7 binary:
* strip /usr/local/lib/libpython2.7.so.1.0

### Strip the Python 3.6 binary:
* strip /usr/local/lib/libpython3.6m.so.1.0

### First get the script:
* wget https://bootstrap.pypa.io/get-pip.py
 
### Then execute it using Python 2.7 and/or Python 3.6:
* python2.7 get-pip.py
* python3.6 get-pip.py
 
# With pip installed you can now do things like this:
* pip2.7 install [packagename]
* pip2.7 install --upgrade [packagename]
* pip2.7 uninstall [packagename]