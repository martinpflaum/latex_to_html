#%%
from core import *
from textfilters import *
from enumitem import *
from latex_equations import *
import os
import sys
from file_loader import *
if len(sys.argv) != 2:
    error_msg()
folder_name = sys.argv[1]

input,bibliography,article_header,discription,out_file = get_files(folder_name)


junk_math = ["\\sffamily","\\textit","\\itshape","\\nolimits","\\nonumber","\\noindent","\\functor","\\textup","\\category","\\indent","\\newpage"]
#replace_mentdict = {"\\noindent":""}#"\\prerequisites ":"</p><h1 style=\"font-size:20px\">Prerequisites</h1><p>","\\N ":"\\mathbb{N}","\\id ":"id","\\GL ":"GL","\\Mat ":"\mathfrak{M}"}
replace_mentdict = {}
junkSearcher = [JunkSearch(elem) for elem in junk_math]
replaceSearcher = [ReplaceSearch(elem,replace_mentdict[elem]) for elem in list(replace_mentdict.keys())]
replaceSearcher.extend([OneArgumentCommandSearch("\\paragraph","<strong>","</strong>"),OneArgumentCommandSearch("\\comments","","")])

basic_expands = []
basic_expands += junkSearcher+replaceSearcher
basic_expands += get_all_textfilters() 
basic_expands += [Enumeration,Itemize]
basic_expands += get_all_latex_searchers()
basic_expands += get_drawtex_searchers()

middle_expands = [OneArgumentJunkSearch(r"\hspace")]



article = convert_latex(input,[basic_expands,middle_expands,[Label],[EqRef,Ref,Cite]])

create_final_file(out_file,article_header,discription,article,bibliography)
