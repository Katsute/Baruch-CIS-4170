#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt


# In[ ]:


nx.draw_networkx(nx.lollipop_graph(10, 5))


# In[ ]:


nx.draw_networkx(nx.balanced_tree(2, 3))


# In[ ]:


nx.Graph()
nx.DiGraph()
nx.MultiGraph()
nx.MultiDiGraph()


# In[ ]:


G = nx.Graph()
G.add_node(1)
G.add_node("Hello World")
nx.draw_networkx(G)


# In[ ]:


G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 4, 6])
nx.draw_networkx(G)


# In[ ]:


G = nx.Graph()
G.add_nodes_from(nx.path_graph(10))
nx.draw_networkx(G)


# In[ ]:


nx.draw_networkx(nx.path_graph(10))


# In[ ]:


G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
nx.draw_networkx(G)


# In[ ]:


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
nx.draw_networkx(G)


# In[ ]:


G = nx.Graph()
G.add_edges_from(nx.path_graph(10).edges)
nx.draw_networkx(G)


# In[ ]:


G.clear()
nx.draw_networkx(G)


# In[ ]:


nx.from_pandas_edgelist(df, source="src", target="targ", edge_attr="attr", create_using=nx.DiGraph())

