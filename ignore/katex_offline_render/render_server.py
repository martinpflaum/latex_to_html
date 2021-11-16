from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def load_file(file_name):
    data = None
    with open(file_name, 'r') as file:
        data = file.read()
    return data


in_file_name = "output.hml"
out_file_name = "rendered.html"

input = load_file(in_file_name)
def preprocess(input,mode):
    input = input.split(f"<span class='{mode}'>")
    go_process = input[0]
    input = input[1:]
    for i,elem in enumerate(input):
        go_process +=f"<span class='{mode}' valindex='{i}'>"+ elem
    return go_process

client_file = input
client_file = preprocess(client_file,"inline")
client_file = preprocess(client_file,"display")
client_file = load_file('xwrapper.html').replace("XXXrender_eqXXX",client_file)

@app.route('/pycall_tex')
def pycall_tex():
    content = request.args.get('content', 0, type=str)
    index = request.args.get('index', 0, type=str)
    
    print(content)
    return jsonify(result="ok")


@app.route('/pycall_finish')
def pycall_finish():
    pass

@app.route('/')
def index():
    return client_file




import webbrowser
print("opening localhost")
url = "http://127.0.0.1:5000/"
webbrowser.open(url)
app.run()
    
# %%
