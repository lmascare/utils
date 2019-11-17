# Build a new Linux / Unix System

 - Load the OS
 - Patch to the latest version
 - Update /etc/skel/.bashrc
```text
alias h=history
alias e=exit
alias c=clear
alias vi=vim
alias p="ps -eaf | egrep $1"

set -o vi
set -o ignoreeof

PATH=$PATH:/opt/bb/bin
EDITOR=/usr/bin/vi
PAGER=/usr/bin/less

export EDITOR PAGER PATH
```
 - Update ~root/.bashrc with same customizations.
 - Create FS
   - /u
   - /db/mysql
   - /db/postgres

 - Create directory structures
```text
/u (contains admin as toplevel directory)
  admin      751   root:oper
  admin/bin  751   oper:oper
  admin/cfg  751   oper:oper
  admin/etc  751   oper:oper
  admin/keys 770   oper:oper
  admin/logs 771   oper:oper
  admin/tmp  771   oper:oper

  # Toplevel directory for users
  users      755   root:root
```

 - Create groups
 ```text
groupadd -g 4000 oper
groupadd -g 4001 mysql
groupadd -g 4002 postgres
```

 - Create user accounts
 ```text
useradd -c 'Operations Automation' -d /u/users/oper -g 4000 -m -k /etc/skel \
-s /bin/bash -u 4000 oper

useradd -c 'Larry Mascarenhas' -d /u/users/lmascare -g 4000 -m -k /etc/skel \
-s /bin/bash -u 6001 lmascare

useradd -c 'MySQL Database' -d /u/users/mysql -g 4001 -m -k /etc/skel \
-s /bin/bash -u 4001 mysql

useradd -c 'Postgres Database' -d /u/users/postgres -g 4002 -m -k /etc/skel \
-s /bin/bash -u 4002 postgres
```

 - Set passwords and expiration policy
```text
 - set passwords for oper, mysql, postgres, lmascare
 - /etc/login.defs for expiration
 - Enable logging of SU, FAILLOG_ENAB, LOG_UNKFAIL_ENAB, SULOG_FILE
 - Update PATH to include /opt/bb/bin
 - Set UMASK to 022
```

 - CRON allowed
```text
cat /etc/cron.allow
oper

```

 - Install Python3 and its modules
```text

```

 - Install MySQL
```

```

 - Install Postgres
 ```
 
 ```

 - Install PERL
```
Download and install from ActiveState - as applicable
```
