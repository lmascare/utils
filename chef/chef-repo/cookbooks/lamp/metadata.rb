name 'lamp'
maintainer 'The Authors'
maintainer_email 'you@example.com'
license 'All Rights Reserved'
description 'Installs/Configures lamp'
long_description 'Installs/Configures lamp'
version '0.1.1'
chef_version '>= 12.1' if respond_to?(:chef_version)

# The `issues_url` points to the location where issues for this cookbook are
# tracked.  A `View Issues` link will be displayed on this cookbook's page when
# uploaded to a Supermarket.
#
issues_url 'https://lmascare-centos.kellynoah.com/larrymasc/lamp/issues'

# The `source_url` points to the development repository for this cookbook.  A
# `View Source` link will be displayed on this cookbook's page when uploaded to
# a Supermarket.
#
source_url 'https://lmascare-centos.kellynoah.com/larrymasc/lamp'

support 'ubuntu'
depends 'httpd', '~> 0.4'
depends 'mysql', '~> 8.0'
depends 'mysql2_chef_gem', '~> 2.0'
depends 'database', '~> 6.0'
