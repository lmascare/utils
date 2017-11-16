#
# Cookbook:: infra
# Recipe:: default
#
# Copyright:: 2017, The Authors, All Rights Reserved.
#
# This recipe will do the following
# Create user accounts
#  - splunk
#  - jenkins
#  - web_admin
# Create the directory structure
#  /u/admin <base dir>
#    |
#    |- bin:751
#    |- cfg:750
#    |- data:751
#    |- etc:751
#    |- keys:750
#    |- logs:775
#    |- tmp:775
#

# User accounts

# splunk
group 'splunk' do
  gid 8080
end

user 'splunk' do
  comment   'Splunk User'
  uid       8080
  group     'splunk'
  home      '/home/splunk'
  password  '$1$MlkxcCGk$iHr/1zCuFyR/qeSwKdLzE1'
  system    true
  shell     '/bin/bash'
end

# jenkins
group 'jenkins' do
  gid 982
end

user 'jenkins' do
  comment   'Jenkins Automation Server'
  uid       986
  group     'splunk'
  home      '/var/lib/jenkins'
  password  '$1$MlkxcCGk$iHr/1zCuFyR/qeSwKdLzE1'
  system    true
  shell     '/bin/false'
end

# web_admin
group 'web_admin' do
  gid 8888
end

user 'web_admin' do
  comment   'Owner of Web Files'
  uid       8888
  group     'web_admin'
  home      '/home/web_admin'
  system    true
  shell     '/bin/false'
end
