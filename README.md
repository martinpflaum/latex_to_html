# latex to html
This is an alpha version of a compiler from latex to html. I will update this repository in September and add more Documentation and make running the programm a bit simpler.
# usage:
python .\main.py --tex_file=in.tex --biblio=bib.bibtex --discription=disc.txt --article_header=artheader.txt --out=out.html

This programm runs only with python3! so you may replace python with python3 if you have python2 installed

For help type python main.py --help

the odering of --key=val doesn't matter
so 


python main.py --tex_file=in.tex --out=out.html



is equal to 


python main.py --out=out.html  --tex_file=in.tex

# state of development:

features included right now
- inplace execution of defined theoremenviroments and commands
- enumerations,sections,subsections,equations (see example.html :) )

features that will be added
- nested enumerations
- a progamm with which you can create diagramms with latex equations in it using katex and svg
- documentation
- better structure of the python files



# used code:
we are using distill for styles since it looks really good https://github.com/distillpub/template
we are using katex for visualization of equations https://github.com/KaTeX/KaTeX



# example
The example is from [Markus Pflaum](https://www.colorado.edu/math/markus-pflaum)

Website

http://www.libermath.org/ShortNotesMathematics/

Latex Code

https://gitlab.com/MarkJoe/ShortNotesMathematics

# emergency backup:
If any styles are running offline in some distant future you will need to manually set the stylefile provided in emergency_backup.zip