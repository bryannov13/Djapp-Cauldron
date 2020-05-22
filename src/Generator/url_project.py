from os import path as p
from os import makedirs

class url_project_generator():
    
    def __init__(self, app, model_name):
        self.txt=[]
        #self.fields=[]
        
        self.doc = []
        self.model_name = model_name
        self.app_info = app
        #self.form_name = self.model_name+"_form"
        self.__set_default_dependencies()
        self.__set_doc()

    def __set_default_dependencies(self):
        a = [
            "from django.contrib import admin\n"
            "from django.urls import path, include\n"
            "\n",
            "urlpatterns = [\n",
            "\tpath('admin/', admin.site.urls),\n",
            "]\n",
            "\n",
        ]
        self.txt = a
        pass
            
    def __set_doc(self):
        a=[]
        a.append("urlpatterns.extend([\n")
        
        #for the future, for any app name, we will need a loop
        #It will happend when update de json format
        a.append("\tpath('"+self.app_info['name']+"/', include('"+self.app_info['name']+".urls'),name = '"+self.app_info['name']+"'),\n")
        
        a.append("])\n")
        a.append("\n")
        
        self.doc = a
    
    def set_file(self,path):
        """
        if not p.exists(path):
            template_file = open(path,"x")
            self.__set_default_dependencies()
        else:
            template_file = open(path,"a")
            pass
        """
        return open(path,"w")
        pass
    
    def create(self, path="./result", default_fields=False):
        
        if not p.exists(path) :
            makedirs(path,0o777)
        
        path= path+"/urls.py"
            
        model_file = self.set_file(path)
        
        model_file.writelines(self.txt + self.doc)
        
        pass
    pass

class Urls_project_Generator(object):
    def __init__(self,app,project_name,out_path):
        try:
            model_ = url_project_generator(app,project_name)
            model_.create(path= out_path+project_name+"/"+project_name,default_fields=True)
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
    
    s=Urls_project_Generator(app,"project_test")