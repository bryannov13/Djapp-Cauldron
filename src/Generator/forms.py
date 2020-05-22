from os import path as p
from os import makedirs

class forms_generator():
    
    def __init__(self, model_name):
        self.txt=[]
        self.fields=[]
        self.model_name = model_name
        self.form_name = self.model_name+"_form"
    
    
    def __set_default_dependencies(self):
        self.txt.append("from django import forms\n")
        self.txt.append("from .models import *\n")
        self.txt.append("\n")
    
    def set_fields(self,fields):
        self.fields.append("\t\tfields = (\n")
        for field in fields:
            self.fields.append("\t\t\t'"+str(field["name"])+"',\n")
        self.fields.append("\t\t)\n")
        
        
        self.fields.append("\t\tlabels = {\n")
        for field in fields:
            self.fields.append("\t\t\t'"+str(field["name"])+"':'"+str(field["name"])+"',\n")
        self.fields.append("\t\t}\n")
        
    
    def set_file(self,path):
        if not p.exists(path):
            model_file = open(path,"x")
            self.__set_default_dependencies()
            
        else:
            model_file = open(path,"a")
            pass
        
        return model_file
        pass
    
    def create(self, path="./result", default_fields=False):
        
        if not p.exists(path) :
            makedirs(path,0o777)
        path= path+"/forms.py"
            
        model_file = self.set_file(path)
        
        self.txt.append("#"+self.form_name+"\n")
        self.txt.append("class "+self.form_name+"(forms.ModelForm):\n")
        self.txt.append("\tclass Meta:\n")
        self.txt.append("\t\tmodel = "+self.model_name+"\n")
        
        for field in self.fields:
            self.txt.append(field)
        
        self.txt.append("\n")
        self.txt.append("\tdef __init__(self, *args, **kwargs):\n")
        self.txt.append("\t\tsuper("+self.form_name+",self).__init__(*args, **kwargs)\n")
        self.txt.append("\n")
        
            
        
            

        model_file.writelines(self.txt)
        pass
    pass

class Forms_Generator(object):
    def __init__(self,app,project_name,out_path):
        for m in app["tables"]:
            try:
                model_ = forms_generator(m["name"])
                model_.set_fields(m["fields"])
                model_.create(path= out_path+project_name+"/"+app["name"],default_fields=True)
                
            except Exception as e:
                print("Forms:\n")
                print(e)
        
        print("Done...")
        
    pass


if __name__ == "__main__":
    
    app= {
        "name": "EjemploAlv",
        "description": ":v",
        "databaseType": "Sqlite",
        "tables": [
                    {
                        "name": "Persona",
                        "fields": [
                            {
                                "name": "Nombre",
                                "type": "String",
                                "required": "True",
                                "unique":"True" #comentar a samy de agregar este campo
                            },
                            {
                                "name": "Edad",
                                "type": "Integer",
                                "required": "True",
                                "unique":"False" #comentar a samy de agregar este campo
                                
                            }
                        ]
                    },
                    {
                        "name": "Mascota",
                        "fields": [
                            {
                                "name": "Nombre",
                                "type": "String",
                                "required": "True"
                            },
                            {
                                "name": "Propietario",
                                "type": "Persona",
                                "required": "False"
                            }
                        ]
                    }
                ]
            }
    
    s=Forms_Generator(app,"project_test")