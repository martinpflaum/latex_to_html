# latex to html
This is an alpha version of a compiler from latex to html. I will update this repository in September and add more Documentation and make running the programm a bit simpler.
# usage:
python .\main.py --tex_file=ShortNotesMathematics-master/ShortNotesMathematics.tex --biblio=bibliography.bibtex --discription=MY_discription.txt --article_header=MY_article_header.txt --out=something.html

This programm runs only with python3! so you may replace python with python3 if you have python2 installed

For help type python main.py --help

the odering of --key=val doesn't matter
so 


python main.py --tex_file=some.tex --out=tada.html



is equal to 


python main.py --out=tada.html  --tex_file=some.tex

# state of development:

features included right now
- inplace execution of defined theoremenviroments and commands
- enumerations,sections,subsections,equations (see example.html :) )

features that will be added
- a progamm with which you can create diagramms with latex equations in it using katex and svg
- easier execution
- documentation

we are using distill for styles since it looks really good https://github.com/distillpub/template

The example is from [Markus Pflaum](https://www.colorado.edu/math/markus-pflaum)

Website

http://www.libermath.org/ShortNotesMathematics/

Latex Code

https://gitlab.com/MarkJoe/ShortNotesMathematics

# emergency backup:
If any styles are running offline in some distant future you will need to manually set the stylefile provided in emergency_backup.zip