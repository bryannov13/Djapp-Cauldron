from os import path as p
from os import makedirs

class form_generator():
    
    def __init__(self, model_name):
        self.txt=[]
        self.fields=[]
        
        self.doc = []
        self.model_name = model_name
        self.form_name = self.model_name+"_form"
        
        self.__set_doc()
    
    def __set_doc(self):

        a=[
            "{% extends 'base.html' %}\n",
            "\n",
            "{% block title %}"+self.model_name+"{% endblock title %}\n",
            "\n",    
            "{% load crispy_forms_tags %}\n",
            "{% block content %}\n",
            "\n",
            "\n",
            '\t<h4 class="display-5">'+self.model_name+'</h4>\n',
            '\t<hr cl ass="my-4">\n',
            "\n",
            
            '\t<!--Messages section-->\n',
            '\t{% if messages %}\n',
            '\t\t{% for message in messages %}\n',
            '\t\t\t<div class="alert alert-{{ message.tags }}" role="alert">\n',
            '\t\t\t{{ message }}\n',
            '\t\t\t</div>\n',
            '\t\t{% endfor %}\n',
            '\t{% endif %}\n',
            "\n",
            "\n",
            
            '\t<form action="" method="POST">\n',
            '\t\t<div class="row">\n',
            '\t\t\t<div class="col-md-12">\n',
            '\t\t\t\t{% crispy form %}\n',
            '\t\t\t</div>\n',
            '\t\t\t<div class="col-md-2"></div>\n',
            '\t\t\t\t<a href="{% url \''+self.model_name+'_list\' %}" class="btn btn-danger col-md-2 m-2"> <i class="fas fa-undo-alt"></i> Cancelar</a>\n',
            '\t\t\t<div class="col-md-2"></div>\n',
            '\t\t\t\t<button type="submit" class="btn btn-primary col-md-4 m-2"> <i class="far fa-save"></i> Guardar</button>\n',
            '\t\t\t<div class="col-md-2"></div>\n',
            '\t\t</div>\n',
            '\t</form>\n',
            '\t{% endblock content %}\n',
        ]
        
        self.doc = a
    
    def set_file(self,path):
        if not p.exists(path):
            template_file = open(path,"x")
            #self.__set_default_dependencies()
            
        else:
            template_file = open(path,"a")
            pass
        
        return template_file
        pass
    
    def create(self, path="./result", default_fields=False):
        
        if not p.exists(path) :
            makedirs(path,0o777)
        
        path= path+"/form.html"
            
        model_file = self.set_file(path)
        
        model_file.writelines(self.doc)
        pass
    pass

class Forms_Generator(object):
    def __init__(self,app, project_name,out_path):
        try:
            for m in app["tables"]:
                
                print("Cooking Form templates <"+m["name"]+"> ...")
                model_ = form_generator(m["name"])
                model_.create(path= out_path+project_name+"/"+app["name"]+"/templates/"+m["name"],default_fields=True)
        except Exception as e:
            print(e)
            pass
        
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
    
    s=Forms_Generator(app)