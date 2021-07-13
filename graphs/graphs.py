#%%
import os
from graphs_core import graph_to_svg,create_final_file

source = """
digraph G {
  { 
    node [margin=0  fontcolor=blue fontsize=12 width=0.8 shape=circle style=filled color=white fixedsize=shape]
    b [label="X_G"]
    a [label="\\sum^4_i i^2"]
    c [label="K_\\varphi"]

  }
  a -> c [class="inline" label="G_\\varphi" len=2.0]
  c -> b [len=2.0]
  b -> a [len=2.0]
  
}
"""
source = source.replace("\\","XXXbackslashXXX")

input = graph_to_svg(source)
#style="background-color:#ffff;"
input = input.replace("<text",'<foreignObject class="inline" width="500" height="500"')
input = input.replace("</text>",'</foreignObject>')
input = input.replace("XXXbackslashXXX","\\")

#input = input.replace("XXX","<foreignObject width='500' height='500' class='inline'>X \\times Y</foreignObject>")
create_final_file(input,"test.html")

# %%
