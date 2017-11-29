## ToDo
 - client.rb change log to a dir
 - Ubunto should have learn_chef_apache
 - Cookbook infra  
    - set directory structure  

## Configuration
* /var/chef directory has
  * backup  \<backup of recipes\>  
  * cache   \<stores cookbooks\>  
* Installation in /opt/chef & /opt/chefdk

## Chef Client
* Create the chef-repo in /u/gitwork/utils/chef-repo  
* chef-client --local-mode motd.rb  

* chef-apply <file.rb>  
  Run the resources in file.rb. But it doesn't know how to apply cookbooks.  
  That's done by chef-client  

* mkdir chef-repo/cookbooks  
* cd chef-repo  
* chef generate cookbook cookbooks/workstation  
* chef generate cookbook cookbooks/apache  

* chef generate cookbook cookbooks/learn_chef_httpd  
* chef generate template cookbooks/learn_chef_httpd index.html  

* chef generate recipe apache server

* Run chef-client in --local-mode  
  __cd cookbooks directory__  
  __sudo chef-client --local-mode -r "recipe[apache::server]"__  
  
* Run multiple recipes  
  __sudo chef-client --local-mode -r "recipe[workstation::setup],recipe[apache::server]"__  

* Run the default recipe from a cookbook
  __sudo chef-client --local-mode -r "recipe[COOKBOOK(::default)]"__

* Include recipe include_recipe
  **include_recipe 'apache::server'**

* Under cookbooks/<cookbook>/recipes/default.rb you can include_recipe

## Chef-client Run
chef-client 
* --> build node --> authenticate --> sync cookbooks (/var/chef/cache)  
* --> load cookbooks (attributes / library / recipe) (builds resource collection )    
* -->  converge  
    * --> success? --> node save  
    * --> fail? --> stop run  
* --> Notification handlers  

## Security Model
* /etc/chef/client.pem
    * Yes --> sign requests
    * No  --> /etc/chef/validation.pem?
        * Yes   --> Request API access --> client.pem
            * Sign requests
        * No    --> Error 401 (Not Authorized)

## Chef Client Attribute Precedence

Location | Attribute Files | Node Recipe | Environment | Role  
--- | --- | --- | --- |  ---
**Levels** |    |    |   |  
 default        | 1  |  2 | 3  |  4
 force\_default  | 5  |  6 |    |  
 normal         | 7  |  8 |    |  
 override       | 9  | 10 |12  | 11  
 force\_override |13  | 14 |    |  
 automatic      | 15 | 15 | 15 | 15
  
## Test Kitchen
**Five stages of test kitchen**  
  1. kitchen create
  2. kitchen converge
  3. kitchen login
  4. kitchen verify
  5. kitchen destroy

* Test are in cookbooks/<cookbook>/test/integration/default/serverspec/default_spec.sh

**kitchen create**  
```apple js
cd cookbooks/learn_chef_httpd
kitchen list
kitchen create
kitchen converge

# Test kitchen
kitchen exec -c 'curl localhost'
```
* Kitchen details in cookbooks/learn_chef_httpd/.kitchen.yml  
* KITCHEN_YAML to define .kitchen.yml file to use


## CHEF Server  
* Download chef-server from chef.io  
  https://downloads.chef.io/chef-server
  
  Installation command  
  rpm -Uvh 'path to rpm file'  
  Installation location is /opt/opscode
  Create a file 'chef' in /etc/profile.d
```angular2html
  if [ -d /opt/opscode/bin ]  
  then  
      PATH=$PATH:/opt/opscode/bin  
      export PATH  
  fi
```
##### Use the link to setup the chef-server
  https://docs.chef.io/install_server.html

##### Important link regarding optional configuration
  https://docs.chef.io/config_rb_server_optional_settings.html

#### Link to the ChefDK
* curl https://omnitruck.chef.io/install.sh # Prefer the rpm
* wget https://packages.chef.io/files/stable/chefdk/2.3.4/el/7/chefdk-2.3.4-1.el7.x86_64.rpm
* rpm -i chefdk-2.3.4-1.el7.x86_64.rpm
* Installed in /opt/chefdk

#### Ensure ssh access from CHEF Server to all nodes
* __Use ssh-keygen to create the key-pair on the chef server  
  and add the id_rsa.pub to the authorized_keys on every node__

#### Setup the Chef Server
* chef-server-ctl reconfigure
  * This will take some time as it re-configures the server
  * Ensure that the hostname is set to the FQDN  
* Create the Unix user & group for 'chef'  
```apple js
groupadd -g 1003 chef
useradd -c 'Chef Automation' -d /home/chef -u 1003 -g 1003 -m -s /bin/bash -k /etc/skel chef
```
* Login as chef and create a .chef directory for the PEM file
```apple js
sudo chef-server-ctl user-create chef CHEF Automation chef@kellynoah.com 'PASSWORD' \
  --filename /users/chef/.chef/chef.pem

# Display list of users 
chef-server-ctl user-list

sudo chef-server-ctl org-create larrymasc 'Larry Mascarenhas' --association_user chef \
  --filename /users/chef/.chef/larrymasc-validator.pem  

```
    **NOTE: Uppercase in org name is not supported**  

* The chef-server-ctl has a list of subcommands to administer the server.
  * chef-server-ctl user-list
  * chef-server-ctl org-list
* URL https://172.31.251.63/organizations/larrymasc
* Ensure that ports 80, 443, 8000 are not used
* Enable access from everywhere
```angular2html
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --reload
firewall-cmd --list-all
```

### Understanding the CHEF Server
#### Omnibus package
**GitHub**  https://github.com/chef/chef-server

  Item   |  Location
 --- | ---
 User config | /etc/opscode  
 pkg installed    | /opt/opscode
 commands     | /opt/opscode/bin
 services     | /opt/opscode/sv
 aux cmds & binaries   | /opt/opscode/embedded/bin
 cookbooks for 'recongure' | /opt/opscode/embedded/cookbooks
 Data and non editable cfg | /var/opt/opscode
 Log files    | /var/log/opscode
 Init master  | 
 RHEL5    | /etc/inittab
 RHEL6 & Ubuntu   | /etc/init
 RHEL7            | /usr/lib/systemd/system

**Data**  
 Item | Location | Notes
 ---  |  ---  |  ---  
 PostgreSQL | opscode_chef | Used by Erchef (Tables: nodes, cookbooks, user environments etc)
   | bifrost | BiFrost (AuthZ) database
   | reporting | Reporting database (Node run history)
 Solr |  | Node is flatened and inserted into Solr for fast searching
 RabbitMQ | Expander queue | node data waiting for ETL before insertion into Solr
    | Analytics Queue | API Actions are stored waiting for ETL by an Analytics Server
      
  
#### Chef Workstation
* knife is the cli interface between workstation and Chef Server
* Requires 2 files to authenticate. Located in .chef directory.
    * RSA private key
    * knife configuration file - knife.rb
* Create a knife.rb file in $HOME/.chef directory
```angular2html
current_dir = File.dirname(__FILE__)
log_level               :info
log_location            STDOUT
node_name               "chef"
client_key              "#{current_dir}/chef.pem"
chef_server_url         "https://lmascare-centos.kellynoah.com/organizations/larrymasc"
cookbook_path           ["#{current_dir}/../cookbooks"]
```    
* Verify connection of workstation to server
```angular2html
knife ssl fetch
knife ssl check
```
* Upload the cookbook created earlier ie learn_chef_httpd
```angular2html
cd cookbooks
knife cookbook upload learn_chef_httpd
knife cookbook list
``` 

#### Chef Client Setup
* Create the chef group and user similar to Chef Server setup
* Copy the chef server id_rsa.pub key to the node's $HOME/.ssh/authorized_keys file

* Ensure that chef has sudo privileges in /etc/sudoers
* Add username to sudo(ubuntu), wheel(centos) group in /etc/group
* _Ubuntu_: /etc/sudoers Add __chef    ALL=(ALL) NOPASSWD: ALL__ 
  _Centos_: /etc/sudoers Uncomment __wheel line which has NOPASSWD__

* Bootstrap the workstation. Works for Centos as the recipe is for Centos.  
  Ubuntu does not use httpd. Instead it is apache2.  
* It will install chef-client and run the listed recipe   
```apple js
knife bootstrap lmascare-centos --ssh-user chef --sudo --node-name lmascare-centos \
    --run-list 'recipe[learn_chef_httpd]' -y
knife bootstrap lmascare-hp --ssh-user chef --sudo --node-name lithium -y
knife bootstrap silicon --ssh-user chef --sudo --node-name silicon -y
knife node list

# To delete the node's metadata
knife node delete <node-name> --yes

# To delete the entry (including RSA Public Key) from Chef Server's API client list
knife client delete <node-name> --yes
knife node show <node-name>
```

* Once cookbooks are uploaded to the chef-server, they can be run using chef-client on the node.  
  But from the chef-server, it is preferable to run knife ssh  
```apple js
knife ssh 'name:lmascare-centos' 'sudo chef-client' --ssh-user chef --attribute ipaddress
sudo chef-client
```
  * Attributes are in 
    * https://docs.chef.io/attributes.html#automatic-ohai  
  
#### Download from Chef Supermarket
* Create a Berksfile 
```apple js
source   'https://supermarket.chef.io'
cookbook 'chef-client'
```
```apple js
# Download the chef-client cookbooks from the Supermarket
# into the $HOME/.berkshelf
berks install

# Upload these cookbooks to the Chef Server
berks upload
```
* Roles enable you to focus on the function the node performs collectively
* Create a role web.json
```apple js
knife role from file roles/web.json
knife role list
knife role show web
knife node run_list set lmascare-centos "role[web]"
knife node show lmascare-centos --run-list
knife ssh 'role:web' 'sudo chef-client' --ssh-user chef --attribute ipaddress
knife status 'role:web' --run-list

# To delete a roles
knife role delete web --yes
```
* To delete a cookbook from the server
```apple js
knife cookbook delete learn_chef_httpd --all --yes
```
* To delete the RSA private key from the node
```apple js
sudo rm /etc/chef/client.pem
```
####**Install additional packages from https://packages.chef.io**  
**To add support for databags, attributes, runlists, roles, environments, and cookbooks from a 
web server interfac**
```apple js
sudo chef-server-ctl install chef-manage
sudo chef-server-ctl reconfigure
sudo chef-manage-ctl reconfigure --accept-license
```

**Add reporting**
```apple js
sudo chef-server-ctl install opscode-reporting
sudo chef-server-ctl reconfigure
suod opscode-reporting-ctl reconfigure
```

**Install packages from a local directory**
```apple js
sudo chef-server-ctl install chef-manage --path=/path/to/file
```
 
**Update CHEF Server to support > 25 nodes**
```apple js
vi /etc/opscode/chef-server.rb
license['nodes'] = 100
```

#### Create an admin chef node
```apple js
tar up the contents of /home/chef/.chef on lmascare-centos and extract on target
```
**Install the Opscode Jobs Push Server**
**It allows you to push jobs independant of the chef-client run**
```apple js
# Download from https://downloads.chef.io/push-jobs-server/ubuntu/

sudo dpkg -i opscode-push-jobs-server_1.1.6-1_amd64.deb
sudo chef-server-ctl install opscode-push-jobs-server
sudo chef-server-ctl reconfigure
sudo opscode-push-jobs-server-ctl reconfigure
```
