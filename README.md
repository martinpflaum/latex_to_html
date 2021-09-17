# latex to html
This is an alpha version of a compiler from latex to html. It is heavily under development and things are going to be changed :D. This projected is not related with distill, we just use their code because its great. I will update this repository in September and add more Documentation and make running the programm a bit simpler.
# usage

USAGE: python main.py path/to/folder

in this folder there need to be certain things:

1. the main tex file called input.tex
2. a bibliography called bibliography.bibtex - make it empty if you are not citing anyone
3. a discription called discription.txt
4. a article_header called article_header.txt 


the article_header is in a really simple file format just look at the given example

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
If any styles are running offline in some distant future you will need to manually set the stylefiles in the html code with the files in emergency_backup.zip
