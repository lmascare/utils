apt_update 'Update the apt cache daily' do
  frequency 86_400
  action :periodic
end

package 'apache2'

service 'apache2' do
  supports  :status => true
  action [:enable, :start]
end

file '/var/www/html/hello.html' do
  content '<html>
  <body>
      <h1>Hello World>/h1>
  </body>
  </html>'
end
