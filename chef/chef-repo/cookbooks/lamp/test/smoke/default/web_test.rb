# # encoding: utf-8

# Inspec test for recipe lamp::web

# The Inspec reference, with examples and extensive documentation, can be
# found at http://inspec.io/docs/reference/resources/

unless os.windows?
  # This is an example test, replace with your own test.
  describe user('root')  do
    it { should exist }
  end
end

# Ensure the 'apache2' package is installed
#
describe package('apache2') do
  it  { should be_installed }
end

# The apache2 service should be enabled and running
describe service 'apache2-default' do
  it  { should be_enabled }
  it  { should be_running }
end

# Test retrieving a test page
describe command 'wget -qSO- --spider localhost' do
  its('stderr')  { should match %r{HTTP/1\.1 200 OK} }
end

# This is an example test, replace it with your own test.
describe port 80 do
  it { should be_listening }
end
