service 'apache2' do
  supports  :status => true
  action [:stop, :disable]
end
