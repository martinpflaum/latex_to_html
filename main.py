#%%
from core import *
from textfilters import *
from enumitem import *
from latex_equations import *
import os
import sys


junk_math = ["\\noindent","\\functor","\\textup","\\category","\\indent","\\newpage"]
#replace_mentdict = {"\\noindent":""}#"\\prerequisites ":"</p><h1 style=\"font-size:20px\">Prerequisites</h1><p>","\\N ":"\\mathbb{N}","\\id ":"id","\\GL ":"GL","\\Mat ":"\mathfrak{M}"}
replace_mentdict = {}

junkSearcher = [JunkSearch(elem) for elem in junk_math]
replaceSearcher = [ReplaceSearch(elem,replace_mentdict[elem]) for elem in list(replace_mentdict.keys())]
replaceSearcher.extend([OneArgumentCommandSearch("\\paragraph","<strong>","</strong>"),OneArgumentCommandSearch("\\comments","","")])

def get_subdic(directory):
    out = []
    for item in os.walk(directory):
        if os.path.isdir(item[0]):
            out += [item[0]]
    return out

def splitargs_in_key_val():
    out = {}
    for arg in sys.argv:
        if arg[:2] == "--":
            arg = arg[2:]
            key,val = arg.split("=")
            out[key] = val
    return out

args = splitargs_in_key_val()
if not "tex_file" in args.keys():
    raise RuntimeError("usage: python main.py --tex_file=parh/to/input.tex --biblio=parh/to/bibliography.bibtex")

file_name = args["tex_file"]
bib_file = args["biblio"]
#"ShortNotesMathematics-master/ShortNotesMathematics"

folder_name = os.path.dirname(file_name)


input = load_latex_file(file_name,get_subdic(folder_name),[])
#ShortNotesMathematics-master/ShortNotesMathematics

article = convert_latex(input,[[JunkSearch("\sffamily")],[Section,Para],[Subsection_star],[Proof],[Emph,Textbf],[Enumeration],get_all_latex_searchers(),junkSearcher,replaceSearcher,[Label],[Ref,Cite]])
_author_header = authors_header({"Markus Pflaum":"htpps"},{"Universität":"htpps"})
_article_header = article_header("Algebraic K-Theory in Low Degrees")

bibliography = load_file(bib_file)
create_final_file("test23.html",_author_header,_article_header,article,bibliography)

# %%
