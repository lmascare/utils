#  Python Tips

#### Virtualenv Python 2.7
 * wget https://bootstrap.pypa.io/get-pip.py 
 * python get-pip.py (Make sure python is for v2.7.x
 * pip install virtualenv
 * virtualenv <envname>
 * source <envname>/bin/activate (this will enable the new virtualenv)
 * deactivate (exit the virtualenv)
 
#### Virtualenv Python 3.6.3
 * python3 -m venv \<virtualenv_dir\>
 * pip3 is already part of Python3.6.3
 * source <virtualenv>/bin/activate
 * deactivate

#### Update pip for TLS/SSL issuues
 * sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
 * pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
 
#### Setup local PyPi server
 * pip download pypiserver
 # TODO

#### List Functions in a module
dir(module)

#### Help on a module
help(module)

**To get the list of packages in a Virtualenv & save in requirements.txt**  
**This .txt file can be used to build your env to move to production**

 * pip freeze > requirements.txt
 * pip install -r requirements.txt

 * Docstrings conformance is checked via pep257, now pydocstyle
 * pip install pep257
 * pip install pydocstyle

 * Code conformance to pep8 is checked via pep8, now pycodestyle
 * pip install pep8

 * Flake incorporates both pep8 & pep257
 * To add support for docstrings in flake8, add the plugin
 * pip install flake8-docstrings

 * Install setuptools
 * Download setuptools tarball.
 * python3 setup.py install

 * Install netifaces. This requires python3-dev
 * python3 setup.py install

 * To get the interfaces
 * python3
   * import netifaces
   * netifaces.interfaces()
   *  ['lo', 'enp0s3']

>>> netifaces.ifaddresses('enp0s3')
{17: [{'addr': '08:00:27:3f:2e:61', 'broadcast': 'ff:ff:ff:ff:ff:ff'}], \
  2: [{'addr': '10.0.2.15', 'netmask': '255.255.255.0', 'broadcast': '10.0.2.255'}], \
 10: [{'addr': 'fe80::856c:a7d7:5d70:9ec4%enp0s3', 'netmask': 'ffff:ffff:ffff:ffff::/64'}]}
>>> ipaddr = addr[netifaces.AF_INET]
>>> ipaddr
[{'addr': '10.0.2.15', 'broadcast': '10.0.2.255', 'netmask': '255.255.255.0'}]
>>> ipaddr[0]
{'addr': '10.0.2.15', 'broadcast': '10.0.2.255', 'netmask': '255.255.255.0'}
>>> ipaddr[0]['addr']
'10.0.2.15'
>>> netifaces.gateways()
{'default': {2: ('10.0.2.2', 'enp0s3')}, 2: [('10.0.2.2', 'enp0s3', True)]}
>>>
#
#
# Lists & dictionaries
my_list = ["cherries", "bananas", "apples"]
my_list[0]
my_list[1]
my_list[-1]
my_list[0:2]
my_list[:]
my_list[::-1]

my_dict = {"Jessica": "cherries", "Tom": "bananas", "Adam": "apples"}
my_dict["Jessica"]
my_dict["Jessica"] = "Pomegranate"

# Using lists or sets
# Lists --> You want to preserve the insertion order of the items
# sets  --> Eliminate duplicates (don't care about order)

sudo apt-get install python-matplotlib

# Print formatting
#
# OLD Style
    print ("Logfile is %s/%s" % (logdir, logfile) )

# NEW Style
    print ("Logfile is {}/{}".format(logdir, logfile) )

# To run os commands, use the subprocess module
# import subprocess
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
# subprocess.call(["ls","-l"])
#
# for pipes, use Popen.communicate() method

# From Python cookbook
   out_bytes = subprocess.check_output(['netstat', '-an'])
except subprocess.CalledProcessError as e:
   out_bytes = e.output # Output generated before error
   code = e.returncode  # Return code

# To redirect STDERR to STDOUT
out_bytes = subprocess.check_output(['netstat','-an'],
                                    stderr = subprocess.STDOUT)

# To execute a command with a timeout
    out_bytes = subprocess.check_output(['netstat','-an'], timeout = 3)
except subprocess.TimeoutExpired as e:

# Star operator
# data in the star variable is always a list
#
def drop_first_last(grades)
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '732-555-1212', '908-555-1212')
print(phone_numbers)
['732-555-1212', '908-555-1212']


# Modules
# Controlling the export

# somemodule.py
def spam();
    pass

def grok():
    fail

blah = 42

# Only export spam and grok

__all__ = ['spam', 'grok']
