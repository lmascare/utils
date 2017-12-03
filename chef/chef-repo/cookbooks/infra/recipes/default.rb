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
#
# ToDo
#
# Variable for HOME so that $HOME/.ssh
# can be used
#
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
  comment      'Jenkins Automation Server'
  uid          986
  group        'jenkins'
  home         '/var/lib/jenkins'
  password     '$1$MlkxcCGk$iHr/1zCuFyR/qeSwKdLzE1'
  system       true
  manage_home  true
  shell        '/bin/bash'
  action       :create
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

# Create .ssh directory for Jenkins
directory   '/var/lib/jenkins/.ssh' do
  owner     'jenkins'
  group     'jenkins'
  mode      '0700'
  action    :create
end

# Create authorized_keys for Jenkins
file        '/var/lib/jenkins/.ssh/authorized_keys' do
   content  'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFFqffCOHoeUAWlOzoD3m/UtadZdGQza4chh070DT65U22bh/1Kuo0aXGZ4Mv7mTci+ek+M3A2FCHVdr8z0Zl6+nyR//XODNqZBwefWTILTCEIzYTgDJuC4EAM/8zxSHIffscGktw+h8o72bv6IynySApUo8gmoAeFFTBvqXmmWWhxZRDHYK2dJuDyqfEIHRH3XpWQAy0cT7lz0dC6S4iv0Ie8Jv/fYNlgIk3uJcXS4QHcpsT9xhwRNfVAQovBkH2fAHngO+A3jk3+ogM4UoBEHl8OhCTPxEtU7xVI8y7NAOfHw2wLhEXTKBrV7GjANz8c18UEOMTi0mWRJqBUIejF jenkins@lmascare-centos.kellynoah.com'
   owner    'jenkins'
   group    'jenkins'
   mode     '0600'
end

# Create directory for Jenkins Workspace
directory   '/u/jenkins/workspace' do
  owner     'jenkins'
  group     'jenkins'
  mode      '0755'
  recursive true
  action    :create
end
#
# Create /u/admin directory structure
