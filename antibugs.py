#%%
def raw_remove_comments(input):
    """
    takes a raw string
    """
    comment = False
    out = ""
    empty = True 
    for elem in input:
        if comment == False:
            if elem == "%":
                comment = True
                empty = False
            else:
                out += elem
        else:
            if elem == "%":
                if empty == False:
                    comment = False
            else:
                empty = False
        if elem == "\n":
            comment = False
    return out

def no_more_html_bugs(input):
    """
    if <n is any where in your html file there will be a bug...
    so we need to fix that
    """
    input = input.replace("<"," < ")
    input = input.replace(">"," > ")
    return input

def no_more_dolar_bugs_begin(input):
    input = input.replace("\\$","BACKSLASHDOLLAR")
    return input
    
def no_more_dolar_bugs_end(input):
    input = input.replace("BACKSLASHDOLLAR","$")
    return input

def no_more_textup_bugs_begin(input):
    input = input.replace("\\textup","")
    return input
    

def remove_empty_at_begin(input):
    out = 0
    for k,elem in enumerate(input):
        if elem == " " or elem == "\n":
            out = k + 1
        else:
            break
    return input[out:]





def only_two_breaks(input):
    """
    todo fixbugs
    """
    input += "  "
    input = input.split("<br>")
    out = ""
    for elem in input[:-1]:
        
        out += (remove_empty_at_begin(elem)) + "<br>"
    out += input[-1]

    while True:
        tmp = out.replace("<br><br><br>","<br><br>")
        if tmp == out:
            out.replace("<br>","\n<br>")
            return out
        else:
            out = tmp

def no_more_bugs_begin(input):
    input = raw_remove_comments(input)
    input = no_more_html_bugs(input)
    input = no_more_dolar_bugs_begin(input)
    input = no_more_textup_bugs_begin(input)
    return input

def no_more_bugs_end(input):
    input = no_more_dolar_bugs_end(input)
    #input = only_two_breaks(input)
    return input

# %%



# %%

# %%
