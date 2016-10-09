* chef-apply <file.rb> 
  Run the resources in file.rb

* mkdir chef/cookbooks
* cd chef/cookbooks
* chef generate cookbooks workstation
* chef generate cookbooks apache
* chef generate recipe apache server

* Download chef-server from chef.io

**Use the link to setup the chef-server**

https://docs.chef.io/release/server_12-6/install_server.html#standalone

* chef-server-ctl reconfigure
  * This will take some time as it re-configures the server
* sudo chef-server-ctl user-create chef CHEF Automation chef@kellynoah.com 'PASSWORD' --filename /users/chef/chef.pem
* sudo chef-server-ctl org-create larrymasc 'Larry Mascarenhas' --association_user chef --filename larrymasc-validator.pem
   * NOTE: Uppercase in org name is not supported

**Install additional packages from https://packages.chef.io**
* sudo chef-server-ctl install chef-manage
* sudo chef-server-ctl reconfigure
* sudo chef-manage-ctl reconfigure --accept-license

**Install the Opscode Jobs Push Server**
**It allows you to push jobs independant of the chef-client run**
* Download from https://downloads.chef.io/push-jobs-server/ubuntu/
* sudo dpkg -i opscode-push-jobs-server_1.1.6-1_amd64.deb
* sudo chef-server-ctl install opscode-push-jobs-server
* sudo chef-server-ctl reconfigure
* sudo opscode-push-jobs-server-ctl reconfigure
* 
