# NetworkX API tips

Installation location for [NetworkX](https://networkx.github.io/documentation/stable/install.html)

```
pip3 install networkx
pip3 install matplotlib
pip3 install nose

import networkX as nx
import matplotlib.pyplot as plt

# To test networkx
nx.test()

nx.draw(T_sub)
plt.show()
```
In [2]: type(T)
Out[2]: networkx.classes.digraph.DiGraph

In [3]: type(T.nodes())
Out[3]: networkx.classes.reportviews.NodeView

In [4]: T.edges(data=True)
Out[4]: OutEdgeDataView([(1, 3, {'date': datetime.date(2012, 11, 16)}),

In [6]: list(T.edges(data=True))[-1]
Out[6]: (23324, 23336, {'date': datetime.date(2010, 9, 20)})

In [6]: list(T.edges(data=True))[-1]
Out[6]: (23324, 23336, {'date': datetime.date(2010, 9, 20)})

