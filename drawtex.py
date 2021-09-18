from easylatex2image_core import latex_to_image,generate_latexfile
from core import *

def load_file(file_name):
    data = None
    with open(file_name, 'r') as file:
        data = file.read()
    return data

image_count = 0

class DrawTexElement(Element):
    def __init__(self,packages_and_commands,content,parent):
        self.content = content
        self.packages_and_commands = packages_and_commands
        super().__init__("",parent)
    def to_string(self):
        global image_count
        out_file_name = f"image_{image_count}"
        generate_latexfile(self.packages_and_commands,self.content,"output/"+out_file_name+"_texfile.txt")
        try:
            latex_to_image(self.packages_and_commands,self.content,"output/"+out_file_name+".png",dpi=1000,img_type="PNG")
        except:
            print("**********")
            print("**********")
            print("**********")
            print("**********")
            print("**********")
            print(f"*******failed compiling latex at runtime, the latexcode that needs to be displayed by {out_file_name}.png is in {out_file_name}.txt******")
            print("**********")
            print("**********")
            print("**********")
            print("**********")
        out = f"<img src='{out_file_name}.png' width='70%' class='teximg'>"
        
        image_count = image_count + 1
        return out

class DrawTexSearch():
    def __init__(self,packages_and_commands,begin,end):
        self.begin,self.end = begin,end
        self.packages_and_commands = packages_and_commands
    def position(self,input):
        return position_of(input,self.begin)

    def split_and_create(self,input,parent):
        pre,content,post = begin_end_split(input,self.begin,self.end)
        content = self.begin + content + self.end
        return pre,DrawTexElement(self.packages_and_commands,content,parent),post

DEFAULT_PACKAGES_AND_COMMANDS = load_file("DEFAULT_PACKAGES_AND_COMMANDS.txt")

draw_tex_stuff = ["tikzpicture","tikzcd"]

def contains_drawtex(input):
    for stuff in draw_tex_stuff:
        if stuff in input:
            return True
    return False

def get_drawtex_searchers():
    out = []
    out += [DrawTexSearch(DEFAULT_PACKAGES_AND_COMMANDS,r"\begin{tikzpicture}",r"\end{tikzpicture}")]
    out += [DrawTexSearch(DEFAULT_PACKAGES_AND_COMMANDS,r"\begin{tikzcd}",r"\end{tikzcd}")]
    return out



# %%
