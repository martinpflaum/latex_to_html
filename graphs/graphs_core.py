#%%
import os 
#helper funcs
def load_file(file_name):
    latex_file = None
    with open(file_name, 'r') as file:
        latex_file = file.read()
    return latex_file

def create_final_file(input,file_name):
    out = None
    with open('html_code_wrapper_content_old.html', 'r') as file:
        data = file.read()
        out = data.split("XXXcallsplittinpythonXXXX")
    
    with open(file_name, "w") as file:
        file.write(out[0] + input + out[1])

#%%
import os
from graphviz import backend

def compile(source, format,engine = 'neato', renderer=None, formatter=None, quiet=False):
    # engines = ['neato','fdp','circo','dot']
    data = str(source).encode("utf-8")
    out = backend.pipe(engine, format, data,renderer=renderer, formatter=formatter,quiet=quiet)
    return out

def graph_to_svg(source,engine = 'neato'):
    input = compile(source,"svg",engine=engine)
    input = str(input).replace("\\r\\n","\n")
    input = "<svg" + input.split("<svg")[1]
    input = input.split("/svg>")[0]  + "/svg>"
    return input