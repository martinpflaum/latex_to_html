#%%
"""
In case miktex doesn't work you will need to compile the latex code in the output folder byhand to an pdf and
then convert the pdf to png
the function below converts a pdf to an png image :) 
"""

from easylatex2image_core import convert_pdf
convert_pdf("output/something_001",dpi=1000,img_type="PNG")
