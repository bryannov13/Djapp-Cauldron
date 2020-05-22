from os import path as p
from os import makedirs

class url_generator():
    
    def __init__(self, model_name):
        self.txt=[]
        #self.fields=[]
        
        self.doc = []
        self.model_name = model_name
        #self.form_name = self.model_name+"_form"
        
        self.__set_doc()

    def __set_default_dependencies(self):
        a = [
            "from django.urls import path, include\n"
            "urlpatterns = []\n",
            "\n",
        ]
        self.txt = a
        
            
    def __set_doc(self):

        a=[
            "\n",
            "from .views import "+self.model_name+"_view\n",
            "\n",
            "urlpatterns.extend([\n",
            "\tpath('"+self.model_name+"/',"+self.model_name+"_view._list, name = '"+self.model_name+"_list'),\n",
            "\tpath('"+self.model_name+"/add/', "+self.model_name+"_view._form, name = '"+self.model_name+"_insert'),\n",
            "\tpath('"+self.model_name+"/<int:id>/',"+self.model_name+"_view._form, name = '"+self.model_name+"_update'),\n",
            "\tpath('"+self.model_name+"/delete/<int:id>/',"+self.model_name+"_view._delete, name = '"+self.model_name+"_delete'),\n",
            "])\n",
        ]
        
        self.doc = a
    
    def set_file(self,path):
        if not p.exists(path):
            template_file = open(path,"x")
            self.__set_default_dependencies()
        else:
            template_file = open(path,"a")
            pass
        
        return template_file
        pass
    
    def create(self, path="./result", default_fields=False):
        
        if not p.exists(path) :
            makedirs(path,0o777)
        
        path= path+"/urls.py"
            
        model_file = self.set_file(path)
        
        model_file.writelines(self.txt)
        model_file.writelines(self.doc)
        pass
    pass

class Urls_Generator(object):
    def __init__(self,app,project_name,out_path):
        try:
            for m in app["tables"]:
                model_ = url_generator(m["name"])
                model_.create(path= out_path+project_name+"/"+app["name"],default_fields=True)
            pass
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
    
    s=Urls_Generator(app)