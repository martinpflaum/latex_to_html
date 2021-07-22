from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def load_file(file_name):
    data = None
    with open(file_name, 'r') as file:
        data = file.read()
    return data

@app.route('/pycall')
def pycall():
    content = request.args.get('content', 0, type=str)
    
    print("call_received",content)
    return jsonify(result="data from python")

@app.route('/')
def index():
    return load_file("basic.html")



import webbrowser
print("opening localhost")
url = "http://127.0.0.1:5000/"
webbrowser.open(url)
app.run()


"""

<script>
  MathJax = {
  tex: {
    autoload: expandable({
      action: ['toggle', 'mathtip', 'texttip'],
      amscd: [[], ['CD']],
      bbox: ['bbox'],
      boldsymbol: ['boldsymbol'],
      braket: ['bra', 'ket', 'braket', 'set', 'Bra', 'Ket', 'Braket', 'Set', 'ketbra', 'Ketbra'],
      cancel: ['cancel', 'bcancel', 'xcancel', 'cancelto'],
      color: ['color', 'definecolor', 'textcolor', 'colorbox', 'fcolorbox'],
      enclose: ['enclose'],
      extpfeil: ['xtwoheadrightarrow', 'xtwoheadleftarrow', 'xmapsto',
                 'xlongequal', 'xtofrom', 'Newextarrow'],
      html: ['href', 'class', 'style', 'cssId'],
      mhchem: ['ce', 'pu'],
      newcommand: ['newcommand', 'renewcommand', 'newenvironment', 'renewenvironment', 'def', 'let'],
      unicode: ['unicode'],
      verb: ['verb']
    })
  }
};
</script>
"""