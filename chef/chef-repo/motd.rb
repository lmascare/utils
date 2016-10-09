file '/tmp/motd' do
  content "Property of ....

  IPADDRESS  :   #{node['ipaddress']}
  HOSTNAME   :   #{node['hostname']}
  Memory     :   #{node['memory']['total']} 
  CPU Speed  :   #{node['cpu']['0']['mhz']}MHz
  Networks   :   #{node['network']['interfaces']}
  "
  
  mode   '0664'
  owner  'root'
  group  'root'
end
