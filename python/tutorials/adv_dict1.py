#!/usr/bin/python
#

application = {
        'lca': {
                 'cmd_line': '/u/genesys/bin/lca 4999',
                 'username': 'genesys',
               },
        'lmgrd': {
                  'cmd_line': '/u/genesys/bin/lmgrd',
                  'username': 'genesys',
                 },
        }

keys = application.keys()
values = application.values()

# Give you ['lca','lmgrd']
print(keys)
#print(values)

# No foreach in Python. Loop through the array)
for appl in keys:
    print(appl)

print(application['lca']['cmd_line'])

# Good Block
# Here we get the keys for application (lca, lmgrd)
#
for app,u_opts in application.items():
    print(app, u_opts)

# From (lca, lmgrd) we get the keys (cmd_line, username) 
# so we can get the values
#
    for app_opts,app_res in u_opts.items():
        print(app,app_opts)
#
