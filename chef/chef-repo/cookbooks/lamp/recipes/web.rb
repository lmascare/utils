#
# Cookbook:: lamp
# Recipe:: web
#
# Copyright:: 2017, The Authors, All Rights Reserved.

# Create the document_root directory
directory node['lamp']['web']['document_root'] do
	recursive	true
end

# Add the site configuration
httpd_config 'default' do
  source    'default.conf.erb'
end

# Install Apache and start the service
httpd_service  'default' do
  mpm          'prefork'
  action       [:create, :start]
  subscribes   :restart, 'httpd_config[default]'
end

# Install the mod_php5 module
httpd_module   'php7' do
  instance  'default'
  package_name 'php'
end

# Install php5-mysql
package  'php-mysql' do
  action    :install
  notifies  :restart, 'httpd_service[default]'
end


