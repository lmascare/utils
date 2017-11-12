
## Chef User
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


## Test Kitchen
* 4 stages of test kitchen
  1. kitchen create
  2. kitchen converge
  3. kitchen verify
  4. kitchen destroy

* Test are in cookbooks/<cookbook>/test/integration/default/serverspec/default_spec.sh

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
* Use ssh-keygen to create the key-pair on the chef server  
  and add the id_rsa.pub to the authorized_keys on every node

#### Setup the Chef Server
* chef-server-ctl reconfigure
  * This will take some time as it re-configures the server
  * Ensure that the hostname is set to the FQDN  
* Create the Unix user & group for 'chef'  
  * groupadd -g 1003 chef
  * useradd -c 'Chef Automation' -d /home/chef -u 1003 -g 1003 -m -s /bin/bash -k /etc/skel chef
  * login as chef and create a .chef directory for the PEM file
* sudo chef-server-ctl user-create chef CHEF Automation chef@kellynoah.com 'PASSWORD' \
  --filename /users/chef/.chef/chef.pem
* Display list of users 'chef-server-ctl user-list'
* sudo chef-server-ctl org-create larrymasc 'Larry Mascarenhas' --association_user chef \
  --filename /users/chef/.chef/larrymasc-validator.pem  
    **NOTE: Uppercase in org name is not supported**  

* The chef-server-ctl has a list of subcommands to administer the server.
  * chef-server-ctl user-list
  * chef-server-ctl org-list
* URL https://172.31.251.63/organizations/larrymasc
* Ensure that ports 80, 443, 8000 are not used
* Enable access from everywhere
```angular2html
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --add-port=443/tcp --permanent
firewall-cmd --reload
firewall-cmd --list-all
```
####Chef Workstation
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
* Ensure that chef has sudo privileges in /etc/sudoers
* Add username to sudo(ubuntu), wheel(centos) group in /etc/group
* _Ubuntu_: /etc/sudoers Add __chef    ALL=(ALL) NOPASSWD: ALL__ 
  _Centos_: /etc/sudoers Uncomment __wheel line which has NOPASSWD__
* Bootstrap the workstation. Works for Centos as the recipe is for Centos.  
  Ubuntu does not use httpd. Instead it is apache2.
* It will install chef-client and run the listed recipe
```angular2html
knife bootstrap lmascare-centos --ssh-user chef --sudo --node-name lmascare-centos \
    --run-list 'recipe[learn_chef_httpd]' -y
knife bootstrap lmascare-hp --ssh-user chef --sudo --node-name lithium -y
knife node list
knife node delete <node-name> -y
knife node show </node-name>
```

####**Install additional packages from https://packages.chef.io**  
**To add support for databags, attributes, runlists, roles, environments, and cookbooks from a 
web server interfac**
* sudo chef-server-ctl install chef-manage
* sudo chef-server-ctl reconfigure
* sudo chef-manage-ctl reconfigure --accept-license

**Add reporting**
* sudo chef-server-ctl install opscode-reporting
* sudo chef-server-ctl reconfigure
* suod opscode-reporting-ctl reconfigure

**Install packages from a local directory**
* sudo chef-server-ctl install chef-manage --path=/path/to/file 

**Update CHEF Server to support > 25 nodes**
* vi /etc/opscode/chef-server.rb
license['nodes'] = 100



**Install the Opscode Jobs Push Server**
**It allows you to push jobs independant of the chef-client run**
* Download from https://downloads.chef.io/push-jobs-server/ubuntu/
* sudo dpkg -i opscode-push-jobs-server_1.1.6-1_amd64.deb
* sudo chef-server-ctl install opscode-push-jobs-server
* sudo chef-server-ctl reconfigure
* sudo opscode-push-jobs-server-ctl reconfigure
* 
