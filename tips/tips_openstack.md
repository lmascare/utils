# Openstack Tips

[Installation guide](https://docs.openstack.org/install-guide/index.html) 

[Prerequisites](https://docs.openstack.org/mitaka/install-guide-ubuntu/overview.html)

#### Credentials variables
Password Name | Description
--- | ---
Database Password | Root Password
ADMIN_PASS | User 'admin' password
CINDER_DBPASS | DB password for Cinder
CINDER_PASS |User 'cinder' password (Block Storage Service)
DASH_DBPASS | DB password for Dashboard
DEMO_PASS | User 'demo' password
GLANCE_DBPASS | DB password for Glance
GLANCE_PASS | User 'glance' password (Glance Service (Image_)
KEYSTONE_DBPASS | DB Password for keystone (Identity Service)
METADATA_SECRET | Secret for the metadata proxy
NEUTRON_DBPASS | DB Password for neutron (Networking Service)
NEUTRON_PASS | User 'neutron' password
NOVA_DBPASS | DB Password for Nova (Compute Service)
NOVA_PASS | User 'nova' password
PLACEMENT_PASS | User 'placement' password (Placement Service)
RABBIT_PASS | User 'openstack' password (RabbitMQ)

#### Installation Documents

Service | Installation
--- | ---
Keystone (Identity Service) | [Ubuntu](https://docs.openstack.org/keystone/queens/install/index-ubuntu.html)
Glance (Image Service)| [Ubuntu](https://docs.openstack.org/glance/queens/install/)
Nova (Compute Service) | [Ubuntu](https://docs.openstack.org/nova/queens/install/)
Neutron (Networking Service) | [Ubuntu](https://docs.openstack.org/neutron/queens/install/)
Horizon (Dashboard) | [Ubuntu](https://docs.openstack.org/horizon/queens/install/)
Cinder (Block Storage) | [Ubuntu](https://docs.openstack.org/cinder/queens/install/)


## Pre-requisites
```apple js
# Install & Configure RabbitMQ

apt-get install rabbitmq-server
rabbitmqctl add_user openstack <passwd>

# Set read and write permissions
rabbitmqctl set_permissions openstack ".*" ".*" ".*"

# Install memcached
apt-get install memcached python-memcached

# Edit /etc/memcached.conf. Update -l to reflect the mgmt interface so that
# other modules can connect.

systemctl memcached restart
```
## Keystone Installation  

* Ensure MySQL Server is running  (NOT MARIADB)
* apt-get install mysql-server
* mysql -u root -p
    * create databse keystone;
    * GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'DBPASS';
    * GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'DBPASS';
* apt install keystone apache2 libapache2-mod-wsgi
* edit 'connection & token' in /etc/keystone.conf 
```apple js
su -s /bin/sh -c "keystone-manage db_sync" keystone

keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone

keystone-manage bootstrap --bootstrap-password ADMIN_PASS \
  --bootstrap-admin-url http://controller:5000/v3/ \
  --bootstrap-internal-url http://controller:5000/v3/ \
  --bootstrap-public-url http://controller:5000/v3/ \
  --bootstrap-region-id RegionOne

# Configure Apache /etc/apache2/apache2.conf
    Server localhost

# Set these ENV variables

export OS_USERNAME=admin
export OS_PASSWORD=ADMIN_PASS
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_AUTH_URL=http://controller:5000/v3
export OS_IDENTITY_API_VERSION=3

# Install the openstack CLI

apt install python-openstackclient

# Create a Service project for use
openstack project create --domain default --description "Service Project" service
```

## Glance Installation & Configuration

```apple js
mysql -u root -p
create Database glance;
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' IDENTIFIED BY 'GLANCE_DBPASS';

GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%'  IDENTIFIED BY 'GLANCE_DBPASS';

openstack user create --domain default --password-prompt glance

# Provide user glance the 'admin' role
openstack role add --project service --user glance admin

# Create the Glance Image Service
openstack service create --name glance --description "Openstack Image" image

# Create an endpoint
openstack endpoint create --region RegionOne image public http://localhost:9292
openstack endpoint create --region RegionOne image internal http://localhost:9292
openstack endpoint create --region RegionOne image admin http://localhost:9292

apt install glance

# Edit /etc/glance/glance-api.conf and glance-registry.conf files
su -s /bin/sh -c "glance-manage db_sync" glance
service glance-registry restart
service glance-api restart

# 
wget http://download.cirros-cloud.net/0.3.5/cirros-0.3.5-x86_64-disk.img
openstack image create "cirros" \
  --file cirros-0.3.5-x86_64-disk.img \
  --disk-format qcow2 --container-format bare \
  --public
```

## NOVA Installation and Configuration
```apple js
create database nova;
create database nova_api;
create database nova_cell0;

GRANT ALL PRIVILEGES ON nova_api.* TO 'nova'@'localhost' \
  IDENTIFIED BY 'NOVA_DBPASS';
GRANT ALL PRIVILEGES ON nova_api.* TO 'nova'@'%' \
  IDENTIFIED BY 'NOVA_DBPASS';

GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' \
  IDENTIFIED BY 'NOVA_DBPASS';
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' \
  IDENTIFIED BY 'NOVA_DBPASS';

GRANT ALL PRIVILEGES ON nova_cell0.* TO 'nova'@'localhost' \
  IDENTIFIED BY 'NOVA_DBPASS';
GRANT ALL PRIVILEGES ON nova_cell0.* TO 'nova'@'%' \
  IDENTIFIED BY 'NOVA_DBPASS';

openstack user create --domain default --password-prompt nova
openstack role add --project service --user nova admin
openstack service create --name nova --description 'OpenStack Compute' compute

openstack endpoint create --region RegionOne compute public http://localhost:8774/v2.1
openstack endpoint create --region RegionOne compute internal http://localhost:8774/v2.1
openstack endpoint create --region RegionOne compute admin http://localhost:8774/v2.1

openstack endpoint list # Get the <endpoint-id>
openstack endpoint set --url http://localhost:8774/v2.1 <endpoint-id>

openstack user create --domain default --password-prompt placement
openstack role add --project service --user placement admin
openstack service create --name placement --description "Placement API" placement
openstack endpoint create --region RegionOne placement public http://localhost:8778
openstack endpoint create --region RegionOne placement internal http://localhost:8778
openstack endpoint create --region RegionOne placement admin http://localhost:8778

apt install nova-api nova-conductor nova-consoleauth nova-novncproxy nova-scheduler nova-placement-api

su -s /bin/sh -c "nova-manage api_db sync" nova

# Run this command before any cell creation
nova-manage db sync

service nova-api restart
service nova-consoleauth restart
service nova-scheduler restart
service nova-conductor restart
service nova-novncproxy restart
```

## Neutron Installation and Configuration
```apple js

```