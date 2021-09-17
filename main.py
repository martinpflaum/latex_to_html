#%%
from core import *
from textfilters import *
from enumitem import *
from latex_equations import *
import os
import sys

#tikzpicture
#tikzcd
junk_math = ["\\textit","\\itshape","\\nolimits","\\nonumber","\\noindent","\\functor","\\textup","\\category","\\indent","\\newpage"]
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


def error_msg():
    print("Hello there!\n")
    print("USAGE: python main.py path/to/folder\n")
    print("in this folder there need to be certain things:\n")
    print("1. the main tex file called input.tex")
    print("2. a bibliography called bibliography.bibtex - make it empty if you are not citing anyone")
    print("3. a discription called discription.txt")
    print("4. a article_header called article_header.txt\n")
    print("put it there and try again :)\n")
    exit(1)
if len(sys.argv) != 2:
    error_msg()
folder_name = sys.argv[1]
file_name = folder_name+"/input.tex"
bibliography = folder_name+"/bibliography.bibtex"
discription = folder_name+"/discription.txt"
article_header = folder_name+"/article_header.txt"


try:
    # Create target Directory
    os.mkdir("output")
except FileExistsError:
    pass
out_file = "output/website.html"
import shutil
shutil.copy2('icon.png', 'output/icon.png')

article_header = load_file(article_header)
bibliography = load_file(bibliography)
discription = load_file(discription)


print(get_subdic(folder_name))
input = load_latex_file(file_name,get_subdic(folder_name),[])

basic_expands = [Chapter,JunkSearch("\sffamily"),Section,Para,Subsection_star,Proof,Emph,Textbf,Enumeration]+get_all_latex_searchers()+junkSearcher+replaceSearcher
basic_expands += get_drawtex_searchers()
#basic_expands += 
middle_expands = [OneArgumentJunkSearch(r"\hspace")]
article = convert_latex(input,[basic_expands,middle_expands,[Label],[EqRef,Ref,Cite]])

#article_header("Algebraic K-Theory in Low Degrees")

create_final_file(out_file,article_header,discription,article,bibliography)


anoying_msg = ["File is created :) Have fun with your new website.",\
    "Wow friendly randomized messages! How cool is that?",\
    "Mmmh still not working? Too bad."]

import random

print(anoying_msg[random.randint(0,len(anoying_msg)-1)])
print("Your website is ready to use in the output folder.")
# %%


DEFAULT_PACKAGES_AND_COMMANDS = r"""
\usepackage{url}
\usepackage{amsmath} 
\usepackage{dcolumn}
\setcounter{tocdepth}{4}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows}
\usetikzlibrary{intersections}
\usepackage{tikz-cd}
\usetikzlibrary{cd}
"""

#latex_to_image(DEFAULT_PACKAGES_AND_COMMANDS,content,"hey.jpg")
# %%

# %%

