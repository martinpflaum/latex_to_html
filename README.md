# latex to html
This is an alpha version of a compiler from latex to html. I will update this repository in September and add more Documentation and make running the programm a bit simpler.
# usage:
python main.py --tex_file=parh/to/input.tex --biblio=parh/to/bibliography.bibtex

This programm runs only with python3! so you may replace python with python3 if you have python2 installed
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
