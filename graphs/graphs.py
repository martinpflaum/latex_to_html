#%%
import os
from graphs_core import graph_to_svg,create_final_file

def edit_property(input,prop_name,func):
  xin = input.split(prop_name+"=",1)
  out = xin[0] + prop_name + "="
  xin = xin[1]
  xin = xin.split("\"",2)
  out += xin[0]+"\""+func(xin[1])+"\"" + xin[2]
  return out

def add_func(input,k):
  return str(float(input)+k)
from functools import partial

def post_process(input,bgcolor = "white",x_offset=-10,y_offset=-15):
  xinput = input.split("<text")
  input = xinput[0]
  for elem in xinput[1:]:
    if ">" in elem:
      xelem = elem.split(">",1)
      xelem[0] = edit_property(xelem[0],"x",partial(add_func,k=x_offset))
      xelem[0] = edit_property(xelem[0],"y",partial(add_func,k=y_offset))
      

      elem = "<text" + xelem[0] + ">\\colorbox{"+bgcolor+"}{" + xelem[1]
    input += elem
  input = input.replace("<text",'<foreignObject class="inline" width="500" height="500"')
  input = input.replace("</text>",'}</foreignObject>')
  input = input.replace("XXXbackslashXXX","\\")
  return input

def pre_process(source):
  return source.replace("\\","XXXbackslashXXX")


import sys
def splitargs_in_key_val():
    out = {}
    for arg in sys.argv:
        if arg[:2] == "--":
            arg = arg[2:]
            key,val = arg.split("=")
            out[key] = val
    return out

if sys.argv[1] == "--help":
  print("options are")
  print("--graph=file_with_graph.txt --out=graph_output.html")
  exit()


def load_file(file_name):
  data = None
  with open(file_name, 'r') as file:
    data = file.read()
  return data
        
args = splitargs_in_key_val()
out_file = "graph_output.html"
if "out" in args.keys():
  out_file = args["out"]


source = load_file(args["graph"])
source = pre_process(source)
input = graph_to_svg(source)
input = post_process(input)
create_final_file(input,out_file)

# %%
