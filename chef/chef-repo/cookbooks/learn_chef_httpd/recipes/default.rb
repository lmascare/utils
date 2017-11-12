#
# Cookbook:: learn_chef_httpd
# Recipe:: default
#
# Copyright:: 2017, The Authors, All Rights Reserved.
#
package 'httpd'

service 'httpd' do
  action  [:enable, :start]
end

group 'web_admin' do
  gid 8888
end

user 'web_admin' do
  comment   'Owner of Web Files'
  uid       8888
  group     'web_admin'
  home      '/home/web_admin'
  password  '$1$MlkxcCGk$iHr/1zCuFyR/qeSwKdLzE1'
  system    true
  shell     '/bin/bash'
end

template '/var/www/html/index.html' do
  source 'index.html.erb'
  mode   '0644'
  owner  'web_admin'
  group  'web_admin'
end
