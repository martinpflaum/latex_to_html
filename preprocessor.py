#%%
from core import *
import copy
input = load_file("semantic-macros.tex")
toprocess = input + " "

"""
<ol class="enumeration" type="1">
  <li value="(O1)">This is item three.</li>
  <li value="(O2)">This is item fifty.</li>
  <li value="(O3)">
      Something Aweakkjlk
      <ol class="enumeration" type="1">
      <li value="">This is item three.</li>
      <li value="(A5)">This is item fifty.</li>
      <li value="(A6)">This is item one hundred.</li>
    </ol>
  </li>
</ol>
"""
def execute_on_pattern(input,arg_num,command_name,command_pattern):
    input = input.split(command_name)#save_command_split(input,command_name)
    out = input[0]
    input = input[1:]
    #print(command_name)
    for elem in input:
        pattern_instance = command_pattern
        post = elem
        for k in range(arg_num):
            if first_char_brace(post):  
                content,post = split_on_first_brace(post)
                pattern_instance = pattern_instance.replace("#"+str(k+1),content)
            else:
                pattern_instance = pattern_instance.replace("#"+str(k+1),"")
        out += pattern_instance + post
    return out

def do_commands(input):
    toprocess = input
    out = ""
    all_commands = []
    while True:
        pre,post = split_on_next(toprocess,"\\newcommand")
        out += pre 
        if toprocess == pre:    
            print("break")
            break
        
        command_name,post = split_on_first_brace(post)
        arg_num = 0
        if first_char_brace(post,"["):
            arg_num,post = split_on_first_brace(post,"[","]")
            arg_num = int(arg_num)
        command_pattern,post = split_on_first_brace(post)
        toprocess = post
        all_commands.append((arg_num,command_name,command_pattern))

    while True:
        tmp = input
        for arg_num,command_name,command_pattern in all_commands:
            tmp = execute_on_pattern(tmp,arg_num,command_name,command_pattern)
        if tmp == input:
            break
        input = tmp
    return input


#%%
# %%

split_on_next("cacbac","x")
# %%
a = "kjk"
b = a
a
# %%



save_command_split("\\huhua jkk \\kre\n \\hui{","\\hu")

# %%
"#"+str(1)
# %%
