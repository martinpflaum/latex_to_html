
#%%
#http://thenewcode.com/1068/Making-Arrows-in-SVG
import os

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
#<foreignObject class='inline' width="50" height="50">
from graphviz import Digraph
engines = ['neato','fdp','circo','dot']

u = Digraph('unix', filename='output.svg',format="svg",
            node_attr={"shape":"circle","color":"red"}, engine='neato')
u.attr(size='6,6')

u.edge("K", 'A', label='xxxf_Kxxx')
u.edge('M', 'A',label='xxxfxxx')
u.edge('M', 'K',label='\\(K\\)')
from graphviz._compat import text_type

input = str(u.pipe(format="svg")).replace("\\r\\n","\n")
input = "<svg" + input.split("<svg")[1]
input = input.split("/svg>")[0]  + "/svg>"
input = input.replace("xxxfxxx",'<foreignObject class="inline" width="50" height="50"> K_{f_\psi}</foreignObject>')
u.source
#%%

create_final_file(input,"test.html")
u._encoding
# %%
from graphviz import backend

def compile(source, format,engine = 'neato', renderer=None, formatter=None, quiet=False):
    # engines = ['neato','fdp','circo','dot']
    data = str(source).encode("utf-8")
    out = backend.pipe(engine, format, data,renderer=renderer, formatter=formatter,quiet=quiet)
    return out

source = """
digraph G {
  { 
    node [margin=0 fontcolor=blue fontsize=32 width=0.5 shape=circle style=filled]
    b [fillcolor=yellow fixedsize=true label="a very long label"]
    d [fixedsize=shape label="an even longer label"]
  }
  a -> {c d}
  b -> {c d}
}
"""

input = compile(source,"svg")
input = str(input)
input = "<svg" + input.split("<svg")[1]
input = input.split("/svg>")[0]  + "/svg>"
input = input.replace("xxxfxxx",'<foreignObject class="inline" width="50" height="50"> K_{f_\psi}</foreignObject>')


create_final_file(input,"test.html")
#%%
from graphviz import render
render('dot', 'svg', 'test78.gv')  
# %%








from latex2svg import latex2svg
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])  # baseline position in em
print(out['svg'])  # rendered SVG
# %%
import latex2svg
# %%
import urllib


def latex2svg(latexcode):
    """
    Turn LaTeX string to an SVG formatted string using the online SVGKit
    found at: http://svgkit.sourceforge.net/tests/latex_tests.html
    """
    txdata = urllib.urlencode({"latex": latexcode})
    url = "http://svgkit.sourceforge.net/cgi-bin/latex2svg.py"
    req = urlliurllibb2.Request(url, txdata)
    return urllib2.urlopen(req).read()

print(latex2svg("2+2=4"))
print(latex2svg("\\frac{1}{2\\pi}"))

# %%
# %%
