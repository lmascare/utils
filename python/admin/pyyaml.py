#!/usr/local/bin/python3

r"""documentation --> https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation"""

import yaml

documents = """
---
name: The Set of Gauntlets 'Pauraegen'
description: >
    A set of handgear with sparks that crackle
    across its knuckleguards.
---
name: The Set of Gauntlets 'Paurnen'
description: >
  A set of gauntlets that gives off a foul,
  acrid odour yet remains untarnished.
---
name: The Set of Gauntlets 'Paurnimmen'
description: >
  A set of handgear, freezing with unnatural cold.
"""

# print(documents)

employee = """
# Employee records
-  martin:
    name: Martin D'vloper
    job: Developer
    skills:
      - python
      - perl
      - pascal
-  tabitha:
    name: Tabitha Bitumen
    job: Developer
    skills:
      - lisp
      - fortran
      - erlang
"""


# x = yaml.safe_load(employee)
# x = yaml.safe_load_all(documents)
# x = yaml.load_all(documents, Loader=yaml.BaseLoader)
x = yaml.full_load_all(documents)
# print (x)
for y in x:
    print (y)