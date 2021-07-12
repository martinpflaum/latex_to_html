#%%
import os
from graphs_core import graph_to_svg,create_final_file

source = """
digraph G {
  { 
    node [margin=0  fontcolor=blue fontsize=12 width=0.8 shape=circle style=filled color=white fixedsize=shape]
    b [label="a very long label"]
    a [label="an even longer label"]
    c [label="K_\\varphi"]

  }
  a -> c [label="XXX" len=2.0]
  c -> b [len=2.0]
  b -> a [len=2.0]
  
}
"""

input = graph_to_svg(source)
#input = input.replace("XXX","<foreignObject width='500' height='500' class='inline'>X \\times Y</foreignObject>")
create_final_file(input,"test.html")

# %%

# %%
