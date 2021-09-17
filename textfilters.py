from core import *

class Para(SectionEnumerate):
    def __init__(self,modifiable_content,section_number,parent):
        super().__init__(modifiable_content,parent,"para","section")
        self.section_number = section_number
    def label_name(self):
        return self.get_section_enum()[:-1]

    def to_string(self):
        """
        first children ist name of Section
        """

        out = "<br><br><strong>"+ self.get_section_enum()[:-1]+"</strong>"
        
        return out

    @staticmethod
    def position(input):
        return position_of(input,"\\para")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\para")
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        return pre,Para("",section_number,parent),post

    
class Chapter(SectionEnumerate):

    def __init__(self,modifiable_content,section_name,section_number,parent):
        super().__init__(modifiable_content,parent,"chapter","document")
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input):
        return position_of(input,"\\chapter")
            
    @staticmethod
    def split_and_create(input,parent):
        pre,content = split_on_next(input,"\\chapter")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content =  split_on_first_brace(content)
        if "\\chapter" in content:
            content,post = split_on_next(content,"\\chapter")
            post = "\\chapter" + post
        else:
            post = ""
        
        return pre,Chapter(content,name,section_number,parent),post

    def to_string(self):
        """
        first children ist name of Section
        """
        out = "</p><h1 style='font-size:50px;line-height: 80%;'>" + str(self.section_number) + " "+ self.children[0].to_string()  + "</h1><p>"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


    
class Section(SectionEnumerate):

    def __init__(self,modifiable_content,section_name,section_number,parent):
        super().__init__(modifiable_content,parent,"section",["chapter","document"])
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input):
        return position_of(input,"\\section")
            
    @staticmethod
    def split_and_create(input,parent):
        pre,content = split_on_next(input,"\\section")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content =  split_on_first_brace(content)
        if "\\section" in content:
            content,post = split_on_next(content,"\\section")
            post = "\\section" + post
        else:
            post = ""
        
        return pre,Section(content,name,section_number,parent),post

    def to_string(self):
        """
        first children ist name of Section
        """
        out = "</p><h1>" + self.get_section_enum()[:-1] + " "+ self.children[0].to_string()  + "</h1><p>"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out





class Subsection_star(Element):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input):
        return position_of(input,"\\subsection*")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\subsection*")
        name,post = split_on_first_brace(post)
        return pre,Subsection_star(name,parent),post

    def to_string(self):
        out = "</p><h2>"
        for child in self.children:
            out += child.to_string()
        out += "</h2><p>"
        return out

class Label(Element):
    def __init__(self, modifiable_content, parent,label_ref):
        super().__init__(modifiable_content, parent)
        
        if not hasattr(self.search_class(Document).globals,"labels"):
            self.search_class(Document).globals.labels = {}
        
        holder = self.search_attribute_holder("label_name")
        label_name = "label_error"
        if not holder is None:
            label_name = holder.label_name()
        self.search_class(Document).globals.labels[label_ref] = label_name
    
    @staticmethod
    def position(input):
        return position_of(input,"\\label")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\label")
        label_ref,post = split_on_first_brace(post)
        return pre,Label("",parent,label_ref),post

    def to_string(self):
        return ""


class Ref(Element):
    def __init__(self, modifiable_content, parent,label_ref):
        super().__init__(modifiable_content, parent)
        try:
            self.label_name = self.search_class(Document).globals.labels[label_ref]
        except Exception:
            self.label_name = "ref_error"

    @staticmethod
    def position(input):
        return position_of(input,"\\ref")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\ref")
        label_ref,post = split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self):
        return self.label_name


class EqRef(Element):
    def __init__(self, modifiable_content, parent,label_ref):
        super().__init__(modifiable_content, parent)
        try:
            self.label_name = self.search_class(Document).globals.labels[label_ref]
        except Exception:
            self.label_name = "ref_error"

    @staticmethod
    def position(input):
        return position_of(input,"\\eqref")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\eqref")
        label_ref,post = split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self):
        return self.label_name

class Proof(Element):
    def __init__(self,modifiable_content,parent):
        self.name = "Proof"
        if not split_rename(modifiable_content) is None:
            self.name,modifiable_content = split_rename(modifiable_content) 
        self.name += "."
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(input):
        if "\\begin{proof}" in input:
            return position_of(input,"\\begin{proof}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(input,parent):
        pre,content,post = begin_end_split(input,"\\begin{proof}","\\end{proof}")
        return pre,Proof(content,parent),post

    def to_string(self):
        out = f"<br><i>{self.name}</i>"
        for child in self.children:
            #print(type(child))
            out += child.to_string()
        return out

    
class Textbf(Element):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input):
        return position_of(input,"\\textbf")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\textbf")
        name,post = split_on_first_brace(post)
        return pre,Textbf(name,parent),post

    def to_string(self):
        out = "<strong>"
        for child in self.children:
            out += child.to_string()
        out += "</strong>"
        return out

class Cite(Element):
    def __init__(self,modifiable_content,parent,citations):
        super().__init__(modifiable_content,parent)
        self.citations = citations
    @staticmethod
    def position(input):
        return position_of(input,"\\cite")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\cite")
        name,post = split_on_first_brace(post)
        tmp = ""
        for elem in name.split(" "):
            tmp += elem
        citations = tmp.split(",")
        return pre,Cite("",parent,citations),post

    def to_string(self):
        out = ""
        for elem in self.citations:
            out += "<dt-cite key=\"" + elem +"\"></dt-cite>"
        return out


class Emph(Element):
    def __init__(self,modifiable_content,parent):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input):
        return position_of(input,"\\emph")

    @staticmethod
    def split_and_create(input,parent):
        pre,post = split_on_next(input,"\\emph")
        name,post = split_on_first_brace(post)
        return pre,Emph(name,parent),post

    def to_string(self):
        out = "<i>"
        for child in self.children:
            out += child.to_string()
        out += "</i>"
        return out

