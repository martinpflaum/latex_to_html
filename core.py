import antibugs 
#\numberwithin{equation}{theorem}

"""
class CurlyBrackets(Element):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent)
    
    @staticmethod
    def position(input):
        return position_of(input," {")
    
    @staticmethod
    def split_and_create(input,parent):
        pre,content,post = begin_end_split(input," {","} ")
        out = CurlyBrackets(content,parent)
        return pre,out,post

    def to_string(self):
        out = ""
        for child in self.children:
            out += child.to_string()
        out += ""
        return out"""

def get_all_allchars_no_abc():
    """
    super small subset of - this really makes this programm slow otherwise :D
    allchars_no_abc = [chr(k) for k in range(256)]
    allchars_no_abc = ''.join(allchars_no_abc)
    allchars_no_abc = allchars_no_abc.replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ","")
    allchars_no_abc = allchars_no_abc.replace("abcdefghijklmnopqrstuvwxyz","")
    return allchars_no_abc
    """
    return '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n '


def save_command_split(input,split_on):
    if split_on == "$":
        return input.split("$")
    for appendix in get_all_allchars_no_abc():
        input = input.replace(split_on + appendix,"XXXsplit_meXXX"+appendix)
    input = input.split("XXXsplit_meXXX")
    return input


def remove_empty_at_begin(input):
    out = 0
    for k,elem in enumerate(input):
        if elem == " " or elem == "\n":
            out = k + 1
        else:
            break
    return input[out:]

def find_nearest_classes(input,all_classes):
    """
    returns a list of nearest classes
    """
    min_distance = 99999
    out = []
    for elem in all_classes:
        dist = elem.position(input)
        if dist == -1:
            continue
        else:
            if dist == min_distance:
                out.append(elem)
            if dist < min_distance:
                min_distance = dist
                out = [elem]
        
    if out != []:
        try:
            pass
        except AttributeError:
            pass
    return out

def first_char_brace(input,begin_brace = "{"):
    input = remove_empty_at_begin(input)
    if len(input) == 0:
        return False
    return input[0] == begin_brace

def split_on_first_brace(input,begin_brace = "{",end_brace = "}"):
    """
    input: string with {Something1} Something2
    output: tuple (Something1,Something2)
    """

    input = remove_empty_at_begin(input)
    if len(input) == 0:
        #raise RuntimeError("hi")
        print("first brace empty string ERROR")
        return "ERROR",input
    if input[0] != begin_brace:
        print("first brace NOT Brace ERROR")
        return "ERROR",input

    brace_count = 0
    out1 = ""
    for elem in input:
        out1 += elem
        if elem == begin_brace:
            brace_count = brace_count + 1
        if elem == end_brace:
            brace_count = brace_count - 1
        if brace_count == 0:
            break
    out2 = input[len(out1):]
    out1 = out1[1:-1]
    return out1, out2

def split_rename(input):
    input = remove_empty_at_begin(input)
    if input[0] == "[":
        name,post = split_on_first_brace(input,"[","]")
        return name,post
    else:
        return None


def split_on_next(input,split_on,save_split = True):
    #tmp = input.split(split_on)
    if save_split:
        tmp = save_command_split(input,split_on)
    else:
        tmp = input.split(split_on)
    pre = tmp[0]
    post = input[len(pre + split_on):]
    return pre, post

def begin_end_split(input,beginname,endname):
    """
    """
    pre,elem = split_on_next(input,beginname)
    #elem = beginname + elem
    #middle,post = split_on_first_brace(elem,beginname,endname)

    middle,post = split_on_next(elem,endname)
    return pre,middle,post

def position_of(input,beginname,save_split = True):
    if beginname in input:
        if save_split:
            tmp = save_command_split(input,beginname)
        else:
            tmp = input.split(beginname)
        # tmp = input.split(beginname)
        if len(tmp) == 1:
            return -1
        return len(tmp[0])
    else:
        return -1

class Element():
    """
    #NOTE DO NOT EDIT 
    _children
    _modifiable_content
    """
    children = None
    _modifiable_content = ""
    parent = None
    

    def hasattr(self,input):
        try:
            object.__getattribute__(self,input)
            return True
        except AttributeError:
            return False

    def search_attribute_holder(self,input):
        try:
            object.__getattribute__(self,input)
            return self
        except AttributeError:
            if self.parent is None:
                return None
            else:
                return self.parent.search_attribute_holder(input)

    def all_childs(self):
        out = [self]
        if self.children is None:
            return out
        else:
            for child in self.children:
                out.extend(child.all_childs())
            return out

    def search_on_func(self,function):
        if function(self):
                return self
        else:
            if self.parent is None:
                return None
            else:
                return self.parent.search_on_func(function)

    def search_class(self,input):
        if self.parent is None:
            if isinstance(self,input):
                return self
            else:
                return None
        else:
            if isinstance(self,input):
                return self
            else:
                return self.parent.search_class(input) 
    
    def search_up_on_func(self,function):
        """
        if you are calling this function while the caller is not a child
        of his parent this will throw an error

        - during split_and_create the object will never be a child
        of his parent until it this function is finished!
        """
        if function(self):
            return self
        root = self.search_class(Document)
        all_childs = root.all_childs()
        split_on = -1
        for k,elem in enumerate(all_childs):
            if elem == self:
                split_on = k
                break
        if split_on == -1:
            raise RuntimeError("FATAL ERROR couldn t find own class in roots all_childs " + str(self.__class__))
        all_childs = all_childs[:split_on]

        all_childs = all_childs[::-1]
        for elem in all_childs:
            if function(elem):
                return elem
        return None

    def __getattr__(self, name):
        """if hasattr(self, input):
            return self.__getattr__(name)
        """
        if self.parent is None:
            return None
            #raise AttributeError("No parent in the latex tree has the attribute " + name)
        else:
            return self.parent.__getattr__(name)
    
    def __init__(self,modifiable_content,parent):
        """
        #NOTE PLEASE CALL super().__init__(pre_content,modifiable_content)
        in your child class

        input 
        """
        self._modifiable_content = modifiable_content
        self.parent = parent

    def _finish_up(self):
        """
        this function will be called at the very end 
        it puts modifable_content into an RawText wrapper
        """
        if self._modifiable_content != "":
            if self.children is None:
                self.children = []
            self.children.append(RawText(self._modifiable_content,self))
            self._modifiable_content = ""

        if self.children is None:
            self.children = [RawText(self._modifiable_content,self)]
                #print(type(self))
                #raise RuntimeError("something went wrong children is not none but _modifiable_content != \"")
        else:
            for child in self.children:
                child._finish_up()

    #def develop(self):

    def expand(self,all_classes):
        while True:
            if self._process_children(all_classes) == False:
                break


    def _process_children(self,all_classes):
        """
        #NOTE DO NOT OVERWRITE!!
        
        this function will return True if one child (or grant...grant child) has been updated
        """
        if self._modifiable_content != "":
            if self.children is None:
                self.children = []

            while self._modifiable_content != "":
                selected_classes = find_nearest_classes(self._modifiable_content,all_classes)
                if selected_classes == []:
                    if self.children == []:
                        self.children = None
                        return False
                    element = Undefined(self._modifiable_content,self)
                    self.children.append(element)
                    self._modifiable_content = ""
                else:
                    undefined_string,element,self._modifiable_content = selected_classes[0].split_and_create(self._modifiable_content,self)
                    
                    self.children.append(Undefined(undefined_string,self))
                    self.children.append(element)
            return True
        else:
            if self.children is None:
                return False
            out = False
            for child in self.children:
                out = out or child._process_children(all_classes)
            return out

    def to_string(self):
        """
        output html-string
        """
        raise NotImplementedError("no function to_string found")


class Undefined(Element):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent)

    def to_string(self):
        out = ""
        for child in self.children:
            out += child.to_string()
        return out

class RawText(Element):
    def __init__(self,input,parent):
        super().__init__("",parent)
        self.text = input

    def to_string(self):
        return self.text

def has_value_equal(instance,attribute_name,value):
    if instance.hasattr(attribute_name):
        return (object.__getattribute__(instance,attribute_name)==value)
    else:
        return False

class SectionEnumerate(Element):
    """
    SectionEnumerate Searcher need to implement 
        
    def theorem_enviroment_name(self):
        return "document"

    """
    section_count = 0
    equation_count = 0
    
    def __init__(self,modifiable_content,parent,theorem_env_name,enum_parent_class):
        super().__init__(modifiable_content,parent)
        self.enum_parent_class = enum_parent_class
        self.theorem_env_name = theorem_env_name
    def get_section_enum(self):

        if self.enum_parent_class is None:
            return str(self.section_number) + "."
        else:
            search_func = lambda instance : has_value_equal(instance,"theorem_env_name",self.enum_parent_class)

            section_enum = self.search_up_on_func(search_func)
            if section_enum is None:
                raise RuntimeError("couldn't find enumaration parent: --"+self.enum_parent_class +"-- in enviroment: --" + self.theorem_env_name +"--")

            out = section_enum.get_section_enum()
            out += str(self.section_number) + "."
            return out

    def generate_child_equation_number(self):
        equation_number = self.equation_count + 1
        self.equation_count = self.equation_count + 1
        return equation_number

    def generate_child_section_number(self):
        section_number = self.section_count + 1
        self.section_count = self.section_count + 1
        return section_number



class BeginEquationElement(Element):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent)
    def to_string(self):
        """
        first children ist name of Section
        """
        #\tag{}
        out = "<br><br><span class='display'>"
        for child in self.children:
            out += child.to_string()  
        out += "</span><br><br>"
        return out


class Globals():
    pass




class Document(SectionEnumerate):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent,"document",None)
        self.globals = Globals()
    

    def get_section_enum(self):
        return ""

    @staticmethod
    def position(input):
        if "\\begin{document}" in input:
            return position_of(input,"\\begin{document}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(input,parent):
        pre,content,post = begin_end_split(input,"\\begin{document}","\\end{document}")
        return pre,Document(content,parent),post

    def to_string(self):
        out = ""
        for child in self.children:
            out += child.to_string()
        return out


def load_file(file_name):
    data = None
    with open(file_name, 'r') as file:
        data = file.read()
    
    if "IfFileExists" in data:
        raise RuntimeError("Please remove IfFileExists from " +file_name + " thx.")
    
    return data

def load_latex_file(file_name,visible_paths,loaded_files):
    #file_name = file_name
    if file_name[-4:] != ".tex":
        file_name = file_name + ".tex"
    latex_file = load_file(file_name)
    visible_paths.append(".")
    latex_file = latex_file.split("\input")
    out = latex_file[0]
    for elem in latex_file[1:]:
        name,post = split_on_first_brace(elem)
        if name in loaded_files:
            print("not loading",name)
            out += post
        else:
            tmp = ""
            for path in visible_paths:
                try:
                    loaded_files.append(name)
                    tmp = load_latex_file(path + "/" + name,visible_paths,loaded_files)
                    #print(loaded_files)
                    break
                    #print("Succesfully Loaded File: ",name)
                except FileNotFoundError:
                    pass
            if tmp == "":
                RuntimeError("\\input error File " + name + " could not be found")
            out += tmp + post
    return out
        

def create_final_file(file_name,article_header,discription,article,bibliography):
    out = None
    

    with open('contentwrapper.html', 'r') as file:
        out = file.read()

        out = out.split("XXXarticle_headerXXX")
        out = out[0] + article_header + out[1]
        
        out = out.split("XXXdiscriptionXXX")
        out = out[0] + discription + out[1]
        
        out = out.split("XXXcontentXXX")
        out = out[0] + article + out[1]
        

        out = out.split("XXXbibtexXXX")
        out = out[0] + bibliography + out[1]
  

    with open(file_name, "w") as file:
        file.write(out)

    

def execute_on_pattern(input,arg_num,command_name,command_pattern):
    out = ""
    while(True):
        pattern_instance = command_pattern
        pre,post = split_on_next(input,command_name)
        if input == pre:    
            out += pre
            break
        for k in range(arg_num):
            
            content = ""
            if first_char_brace(post):  
                content,post = split_on_first_brace(post)
            elif first_char_brace(post,"["):
                content,post = split_on_first_brace(post,"[","]")
            pattern_instance = pattern_instance.replace("#"+str(k+1),content)

        input = post
        out += pre + pattern_instance

    return out

def do_commands(input):
    toprocess = input
    out = ""
    all_commands = []
    while True:
        #
        pre,post = split_on_next(toprocess,"\\newcommand")
        out += pre 
        if toprocess == pre:    
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


def execute_enviroment_on_pattern(input,environment_name,arg_num,begin,end):
    out = ""
    while(True):
        begin_instance = begin
        end_instance = end
        if not "\\begin{"+environment_name+"}" in input:    
            out += input
            break

        pre,content,post = begin_end_split(input,"\\begin{"+environment_name+"}","\\end{"+environment_name+"}")
        for k in range(arg_num):
            argument = ""
            if first_char_brace(content):  
                argument,content = split_on_first_brace(content)
            elif first_char_brace(content,"["):
                argument,content = split_on_first_brace(content,"[","]")
            end_instance = end_instance.replace("#"+str(k+1),argument)
            begin_instance = begin_instance.replace("#"+str(k+1),argument)
        input = post
        out += pre + begin_instance + content +  end_instance

    return out


def do_newenvironment(input):
    toprocess = input
    out = ""
    all_env = []
    while True:
        pre,post = split_on_next(toprocess,"\\newenvironment")
        out += pre 
        if toprocess == pre:    
            break
        
        environment_name,post = split_on_first_brace(post)
        arg_num = 0
        if first_char_brace(post,"["):
            arg_num,post = split_on_first_brace(post,"[","]")
            arg_num = int(arg_num)
        post = "{" + split_on_next(post,"{")[1]
        begin,post = split_on_first_brace(post)
        end,post = split_on_first_brace(post)
        toprocess = post
        all_env.append((environment_name,arg_num,begin,end))

    while True:
        tmp = input
        for environment_name,arg_num,begin,end in all_env:
            tmp = execute_enviroment_on_pattern(tmp,environment_name,arg_num,begin,end)
        if tmp == input:
            break
        input = tmp
    return input




class TheoremElement(SectionEnumerate):
    def __init__(self,modifiable_content,section_number,parent,display_name,theorem_env_name,enum_parent_class):
        super().__init__(modifiable_content,parent,theorem_env_name,enum_parent_class)
        self.section_number = section_number 
        self.display_name = display_name
        

    def label_name(self):
        return self.get_section_enum()[:-1]
    
    def to_string(self):
        """
        first children ist name of Section
        """

        out = "<br><br><strong>" + self.display_name + " " + self.get_section_enum()[:-1]+"</strong>"

        for child in self.children:
            out += child.to_string()
        
        out += "<br><br>"
        return out




class TheoremSearcher():
    
    def __init__(self,theorem_env_name,enum_parent_class,display_name):
        self.display_name = display_name
        self.theorem_env_name = theorem_env_name
        self.enum_parent_class = enum_parent_class
    def position(self,input):
        return position_of(input,"\\begin{" + self.theorem_env_name + "}")
            
    def split_and_create(self,input,parent):
        pre,content,post = begin_end_split(input,"\\begin{"+self.theorem_env_name+"}","\\end{"+self.theorem_env_name+"}")
        
        search_func = lambda instance : has_value_equal(instance,"theorem_env_name",self.enum_parent_class)
        section_enum = parent.children[-1].search_up_on_func(search_func)
        section_number = section_enum.generate_child_section_number()
        
        return pre,TheoremElement(content,section_number,parent,self.display_name,self.theorem_env_name,self.enum_parent_class),post

def get_theoremSearchers(input):
    need_fix = []
    pending_envs = []
    shared_parent_fixer = {"section":"document","subsection":"section"}
    while True:
        pre,post = split_on_next(input,"\\newtheorem")
        if input == pre:
            break
        theorem_env_name,post = split_on_first_brace(post)
        display_name = ""
        if first_char_brace(post):
            enum_parent_class = ""
            display_name,post = split_on_first_brace(post)
            if first_char_brace(post,"["):
                enum_parent_class,post = split_on_first_brace(post,"[","]")
            else:
                enum_parent_class = None
            shared_parent_fixer[theorem_env_name] = enum_parent_class
            pending_envs.append((theorem_env_name,enum_parent_class,display_name))
        else:
            if first_char_brace(post,"["):
                shared_parent,post = split_on_first_brace(post,"[","]")
                display_name,post = split_on_first_brace(post)
                need_fix.append((theorem_env_name,shared_parent,display_name))
            else:
                print("theoremenv error in ",theorem_env_name)
        input = post
        
    for theorem_env_name,shared_parent,display_name in need_fix:
        pending_envs.append((theorem_env_name,shared_parent_fixer[shared_parent],display_name))
    
    out = []
    for elem in pending_envs:
        print(elem)
        out.append(TheoremSearcher(*elem))
    return out

def get_number_within_equation(input):
    input = input.split("\\numberwithin{equation}")
    if len(input) == 1:
        return "document" 
    out,_ = split_on_first_brace(input[1])
    return out



class JunkSearch():
    def __init__(self,junk_name,save_split = True):
        self.junk_name = junk_name
        self.save_split = save_split

    def position(self,input):
        return position_of(input,self.junk_name,self.save_split)

    def split_and_create(self,input,parent):
        pre,post = split_on_next(input,self.junk_name,self.save_split)
        return pre,Undefined("",parent),post


def convert_latex(input,all_classes_prio):
    if not isinstance(all_classes_prio[0],list):
        all_classes_prio = [all_classes_prio]
    input = antibugs.no_more_bugs_begin(input)
    input = do_commands(input)
    input = do_newenvironment(input)
    all_classes_prio[0].extend(get_theoremSearchers(input))
    number_within_equation = get_number_within_equation(input)
    

    pre_docmuent,document,post_document = Document.split_and_create(input,None)
    document.globals.number_within_equation = number_within_equation
    
    expand_on = []
    for all_classes in all_classes_prio:
        expand_on.extend(all_classes)

    document.expand(expand_on)
    document.expand([JunkSearch("{",save_split=False),JunkSearch("}",save_split=False)])
    document.expand([JunkSearch("\\ ",save_split=False)])
    #pre_content are just commands
    
    document._finish_up()
    out = document.to_string()
    out = antibugs.no_more_bugs_end(out)    
    
    return out



class ReplaceSearch():
    def __init__(self,junk_name,replacement,save_split=True):
        self.junk_name = junk_name
        self.replacement = replacement
        self.save_split = save_split

    def position(self,input):
        return position_of(input,self.junk_name,self.save_split)

    def split_and_create(self,input,parent):
        pre,post = split_on_next(input,self.junk_name,self.save_split)
        return pre,Undefined(self.replacement,parent),post



class GuardianSearch():
    def __init__(self,name,save_split = True):
        self.name = name
        self.save_split = save_split

    def position(self,input):
        return position_of(input,self.name,self.save_split)

    def split_and_create(self,input,parent):
        pre,post = split_on_next(input,self.name,self.save_split)
        return pre,RawText(self.name,parent),post




class OneArgumentCommandSearch():
    def __init__(self,command_name,begin,end):
        self.command_name,self.begin,self.end = command_name,begin,end

    def position(self,input):
        return position_of(input,self.command_name)

    def split_and_create(self,input,parent):
        pre,post = split_on_next(input,self.command_name)
        name,post = split_on_first_brace(post)
        return pre,Undefined(self.begin + name + self.end,parent),post

