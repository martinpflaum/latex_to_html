from core import *
#\item[something] has no enumeration
#[TAG] changes arguments to [] type
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

class EnumerationItem(Element):
    def __init__(self,modifiable_content,parent,label = None):
        super().__init__("",parent)

        label = ""
        if label is None:
            enumeration = self.search_class(Enumeration)
            label = enumeration.generate_item_label()
        self.label = label
        
        self.children = [Undefined(label,self),Undefined(modifiable_content,self)]
    def label_name(self):
        return self.label#self.children[0].to_string()

    def to_string(self):
        
        out = "<li value='"+self.children[0].to_string()+"'>" 
        self.children = self.children[1:]
        for child in self.children:
            out += child.to_string()
        out += "</li>"
        return out

    @staticmethod
    def position(input):
        return position_of(input,"\\item")
            
    @staticmethod
    def split_and_create(input,parent):
        pre,content = split_on_next(input,"\\item")

        if "\\item" in content:
            content,post = split_on_next(content,"\\item")
            post = "\\item" + post
        else:
            post = ""

        label = None
        if first_char_brace(content,"["):
            label,content = split_on_first_brace(content,"[","]")
        elem_out = EnumerationItem(content,parent,label)
        
        return pre,elem_out,post


def enum_style_roman(index):
    roman = ["i","ii","iii","iv","v","vi","vii","viii","ix","x"]
    return roman[index].upper()

def enum_style_Roman(index):
    roman = ["i","ii","iii","iv","v","vi","vii","viii","ix","x"]
    return roman[index]

def enum_style_arabic(index):
    return str(index + 1)

def enum_style_alph(index):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    return lowercase[index]

def enum_style_Alph(index):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return uppercase[index]

def enum_style_empty(index):
    return ""

enum_styles = {"\\roman":enum_style_roman,"\\Roman":enum_style_Roman,"\\arabic":enum_style_arabic,"\\alph":enum_style_alph,"\\Alph":enum_style_Alph}
       
class Enumeration(Element):
    current_index = 0
    def __init__(self,modifiable_content,parent,style_func,left,right):
        super().__init__(modifiable_content,parent)
        self.style_func,self.left,self.right = style_func,left,right

    def to_string(self):
        out = "</p><ol class='enumeration'>" 
        for child in self.children:
            out += child.to_string()
        out += "</ol><p>"
        return out
    @staticmethod
    def position(input):
        return position_of(input,"\\begin{enumerate}")

    @staticmethod
    def split_and_create(input,parent):
        
        pre,content,post = begin_end_split(input,"\\begin{enumerate}","\\end{enumerate}")
        
        style_func = None
        left = ""
        right = ""
        
        if first_char_brace(content,"["):
            options,content = split_on_first_brace(content,"[","]")
            options_pre,options_post = split_on_next(options,"label")
            options_post = remove_empty_at_begin(options_post)
            options_post = options_post[1:]#remove = 
            options_label = ""
            #print("options_post",options_post)
            if first_char_brace(options_post,"{"):
                options_label,options_post = split_on_first_brace(options_post)
            
            tmp = options_post.split(",")[0]
            options_label = options_label + tmp
            
            for style in enum_styles.keys():
                if style in options_label:
                    style_func = enum_styles[style]
                    tmp = options_label.split(style)
                    left = tmp[0]
                    _,right = split_on_next(tmp[1],"*")
                    break 

            if style_func is None:
                style_func = enum_style_empty
                left = options_label
        else:
            style_func = enum_style_arabic
            right = "."

        left = left.replace("\\sffamily","")
        left = left.replace("{","")
        left = left.replace("}","")
        
        right = right.replace("\\sffamily","")
        right = right.replace("{","")
        right = right.replace("}","")
        

        elem_out = Enumeration(content,parent,style_func,left,right)
        elem_out.expand([EnumerationItem])

        return pre,elem_out,post

    def generate_item_label(self):
        self.current_index = self.current_index + 1
        return self.left + self.style_func(self.current_index-1)+ self.right



