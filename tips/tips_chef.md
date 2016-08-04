* Download chef-server from chef.io

**Use the link to setup the chef-server

https://docs.chef.io/release/server_12-6/install_server.html#standalone

* chef-server-ctl reconfigure
  * This will take some time as it re-configures the server
* sudo chef-server-ctl user-create chef CHEF Automation chef@kellynoah.com 'PASSWORD' --filename /users/chef/chef.pem
* sudo chef-server-ctl org-create larrymasc 'Larry Mascarenhas' --association_user chef --filename larrymasc-validator.pem
   * NOTE: Uppercase in org name is not supported

**Install additional packages from https://packages.chef.io
* sudo chef-server-ctl install chef-manage
* sudo chef-server-ctl reconfigure
* sudo chef-manage-ctl reconfigure --accept-license

* Next is chef Push Jobs
