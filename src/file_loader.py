from core import split_on_first_brace
import os
import sys


def load_file(file_name):
    data = None
    with open(file_name, 'r') as file:
        data = file.read()
    return data

def load_latex_file(file_name,visible_paths,loaded_files):
    #file_name = file_name
    if file_name[-4:] != ".tex":
        file_name = file_name + ".tex"
    latex_file = load_file(file_name)
    visible_paths.append(".")
    latex_file = latex_file.split("\input")
    out = latex_file[0]
    for elem in latex_file[1:]:
        name,post = split_on_first_brace(elem)
        name = name.split("/")[-1]
        name = name.split("\\")[-1]
        
        if name in loaded_files:
            #print("not loading",name)
            out += post
        else:
            tmp = ""
            for path in visible_paths:
                try:
                    tmp = load_latex_file(path + "/" + name,visible_paths,loaded_files+[name])
                    loaded_files.append(name)
                    print("loaded ",name)
                    #print(tmp)
                    break
                    #print("Succesfully Loaded File: ",name)
                except:
                    pass
            if tmp == "":
                RuntimeError("\\input error File " + name + " could not be found")
            out += tmp + post
        
        if not name in loaded_files:
            print("\\input error File " + name + " could not be found")
            
    return out

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


def get_files(folder_name):

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

    bibliography = load_file(bibliography)
    article_header = load_file(article_header)
    discription = load_file(discription)


    print(get_subdic(folder_name))
    input = load_latex_file(file_name,get_subdic(folder_name),[])
    return input,bibliography,article_header,discription,out_file