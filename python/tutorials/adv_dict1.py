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

# print(keys)
# print(values)

# print(application['lca']['cmd_line'])

for app,u_opts in application.items():
    print(app)

#for u_items in u_opts.items():
    #print(u_items)

for nested_items in application.values():
    print(nested_items, nested_items['cmd_line'])
