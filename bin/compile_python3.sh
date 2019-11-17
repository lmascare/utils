#!/bin/bash

# Script to Download and Compile Python
py_ver=$1

if [[ "${py_ver}" == "" ]]
then
        echo "No Version specified. Exiting..."
        exit 1
fi

# Download the file
set -x
cd ../misc

wget http://python.org/ftp/python/${py_ver}/Python-${py_ver}.tar.xz

tar xf Python-${py_ver}.tar.xz

# 2019-11-17. Following options are unrecognized
# --with-threads
# --disable-rpath
#
cd Python-${py_ver}
./configure --prefix=/opt/bb/python_${py_ver} \
 --disable-shared       \
 --enable-optimizations \
 --with-lto             \
 --with-pydebug         \
 --with-system-ffi      \
 --with-system-expat    \
 --enable-loadable-sqlite-extensions 

make
