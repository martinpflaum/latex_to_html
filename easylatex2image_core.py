#%%
import os  
from pdf2image import convert_from_path
import tempfile
import copy
CONTENT_WRAPPER = r"""
\documentclass[a4paper, 10pt]{article}
%%packages%%
\hoffset=-1in
\voffset=-1in
\setbox0\hbox{
%%content%%
}
\pdfpageheight=\dimexpr\ht0+\dp0\relax
\pdfpagewidth=\wd0
\shipout\box0
\stop
"""

def convert_pdf(in_file_name,out_file_name,dpi=500,img_type="JPEG"):
    """
    this function takes as input a pdf_file_name and outputs an image
    """
    
    pages = convert_from_path(in_file_name+".pdf", dpi)
    page = pages[0]
    if not out_file_name is None:
        page.save(f'{out_file_name}', img_type)
    return page
    

def latexfile_to_image(in_file_name,out_file_name,dpi=500,img_type="JPEG"):
    temp_dir = tempfile.TemporaryDirectory()
    file_name = temp_dir.name + "\\something"
    os.system(f"pdflatex --jobname={file_name} {in_file_name}")
    out = convert_pdf(file_name,out_file_name,dpi=dpi,img_type=img_type)
    temp_dir.cleanup()
    return out
def generate_latexfile(packages_and_commands,content,out_file_name):
    data = copy.deepcopy(CONTENT_WRAPPER)
    data = data.replace("%%packages%%",packages_and_commands)
    data = data.replace("%%content%%",content)
        
    with open(out_file_name, "w") as file:
        file.write(data)


def latex_to_image(packages_and_commands,content,out_file_name,dpi=500,img_type="JPEG"):
    """
    this function requires miktex (link: https://miktex.org) to be installed

    input:
    packages_and_commands: string of packages and commands
    content: the content that should be converted to an image
    out_file_name: string or none - if none the image will not be saved
    dpi: resolution of the image. Higher is better but with more storage.
    output:
    pillow Image
    """
    temp_dir = tempfile.TemporaryDirectory()
    file_name = temp_dir.name + "\\something"
    generate_latexfile(packages_and_commands,content,file_name)
    out = latexfile_to_image(file_name,out_file_name,dpi=dpi,img_type=img_type)
    temp_dir.cleanup()
    return out



# %%
