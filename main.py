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

if sys.argv[1] == "--help":
    print("options are")
    print("--tex_file=parh/to/input.tex --biblio=parh/to/bibliography.bibtex --article_header=path/to/MY_article_header.txt --out=something.html --description=MY_disrciption.txt".replace(" ","\n"))
    exit()


args = splitargs_in_key_val()
print(args.keys())
if not "tex_file" in args.keys():
    raise RuntimeError("usage: python main.py --tex_file=parh/to/input.tex --biblio=parh/to/bibliography.bibtex --article_header=path/to/MY_article_header.txt --out=something.html --description=MY_disrciption.txt")

file_name = args["tex_file"]

bibliography = "" 
if "biblio" in args.keys():
    bibliography = load_file(args["biblio"])

article_header = ""
if "article_header" in args.keys():
    article_header = load_file(args["article_header"])
    
out_file = "output.html"
if "out" in args.keys():
    out_file = args["out"]

discription = ""
if "discription" in args.keys():
    discription = load_file(args["discription"])
    print("discription")
#"ShortNotesMathematics-master/ShortNotesMathematics"

folder_name = os.path.dirname(file_name)

print(get_subdic(folder_name))
input = load_latex_file(file_name,get_subdic(folder_name),[])

#ShortNotesMathematics-master/ShortNotesMathematics

article = convert_latex(input,[[JunkSearch("\sffamily")],[Section,Para],[Subsection_star],[Proof],[Emph,Textbf],[Enumeration],get_all_latex_searchers(),junkSearcher,replaceSearcher,[Label],[Ref,Cite]])
#article_header("Algebraic K-Theory in Low Degrees")

create_final_file(out_file,article_header,discription,article,bibliography)

# %%
