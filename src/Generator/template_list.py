from os import path as p
from os import makedirs

class list_generator():
    
    def __init__(self, fields, model_name):
        
        self.fields=fields
        
        self.doc = []
        self.model_name = model_name
        self.form_name = self.model_name+"_form"
        
        self.__set_doc()
    
    def __set_doc(self):
        a=[
            "{% extends 'base.html' %}\n",
            
            "{% block title %}"+self.model_name+"{% endblock title %}\n",
            "\n",
            "{% block content %}\n",
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
            
            '\t<table class = "table table-borderless">\n',
            '\t\t<thead class="border-bottom font-weight-bold">\n',
            '\t\t\t<tr>\n',
        ]
        
        for col in self.fields:
            a.append('\t\t\t\t<td>'+col['name']+'</td>\n')
        
        a.extend([
            
            '\t\t\t\t<td class="action-buttons" style="text-align:center">\n',
            '\t\t\t\t\t<a href="{% url \''+self.model_name+'_insert\'%}" class="btn btn-outline-success float-rigth"> <i class="fas fa-plus-circle"></i> add</a>\n',
            '\t\t\t\t</td>\n',
            
            '\t\t\t</tr>\n',
            '\t\t</thead>\n',
            
            '\t\t<tbody>\n',
            '\t\t\t{% for item in items_list %}\n',
            '\t\t\t\t<tr>\n',
        ])
        
        for col in self.fields:
            a.append('\t\t\t\t\t<td>{{item.'+col['name']+'}}</td>\n')
        
        a.extend([
            '\t\t\t\t\t<td class="action-buttons" style="text-align:center" >\n',
            '\t\t\t\t\t\t<a href="{% url \''+self.model_name+'_update\' item.id %}" class="btn text-primary d-inline center"> <i class="far fa-edit">  </i></a>\n',
            '\t\t\t\t\t\t<form action="{% url \''+self.model_name+'_delete\' item.id %}" method="POST" class="d-inline">\n',
            '\t\t\t\t\t\t\t{% csrf_token %}\n',
            '\t\t\t\t\t\t\t<button type = "submit" class="btn">\n',
            '\t\t\t\t\t\t\t\t<i class="fas fa-trash-alt text-danger"></i>\n',
            '\t\t\t\t\t\t\t</button>\n',
            '\t\t\t\t\t\t</form>\n',
            '\t\t\t\t\t</td>\n',
            '\t\t\t\t</tr>\n',
            '\t\t\t{% endfor %}\n',
            '\t\t</tbody>\n',
            '\t</table>\n',
            '{% endblock content %}\n',
        ])
        
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
        
        path= path+"/list.html"
            
        model_file = self.set_file(path)
        
        model_file.writelines(self.doc)
        pass
    pass

class Lists_Generator(object):
    def __init__(self,app,project_name,out_path):
        try:
            for m in app["tables"]:
                
                print("Cooking List templates <"+m["name"]+"> ...")
                
                model_ = list_generator(m["fields"],m["name"])
                model_.create(path= out_path + project_name+"/"+app["name"]+"/templates/"+m["name"],default_fields=True)
                
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
    
    s=Lists_Generator(app,app['name'])