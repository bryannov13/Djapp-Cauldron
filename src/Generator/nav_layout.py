from os import path as p
from os import makedirs

class nav_generator():
    
    def __init__(self, app, project_name):
        self.txt=[]
        self.fields=[]
        
        self.doc = []
        #self.app_name = app_name
        #self.tables = app['tables']
        self.app = app
        
        self.__set_doc()
    
    def __set_doc(self):

        a=[
            '{% block sidebar %}\n',
            '<nav class="navbar navbar-dark bg-dark">\n',
            '\t<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">\n',
            '\t\t<span class="navbar-toggler-icon"></span>\n',
            '\t</button>\n',
            "\n",
            '\t<div class="collapse navbar-collapse" id="navbarTogglerDemo01">\n',
            '\t\t<a class="navbar-brand" href="#">Home</a>\n',
            '\t\t<ul class="navbar-nav mr-auto mt-2 mt-lg-0">\n',
            '\t\t\t<li class="nav-item">\n',
            '\t\t\t\t<a class="nav-link" href="../">Home</a>\n',
            '\t\t\t</li>\n',
            "\n",
            '\t\t\t{% with url="http://localhost:8000/"%}\n',
            "\n",
            '\t\t\t<li class="nav-item active dropdown">\n',
            '\t\t\t\t<a class="nav-link dropdown-toggle" href="{{url}}/#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'+self.app['name']+'</a>\n',
            '\t\t\t\t<div class="dropdown-menu bg-dark" aria-labelledby="navbarDropdown">\n',
            '\t\t\t\t\t<div class="dropdown-divider nav-link"></div>\n',
            
        ]
        
        for model in self.app['tables']:
            a.extend([
                    '\t\t\t\t\t<a class="dropdown-item nav-link" href="{{url}}'+self.app['name']+'/'+model['name']+'">'+model['name']+'</a>\n',
            ])
            
        a.extend([
            '\t\t\t\t\t<div class="dropdown-divider nav-link"></div>\n',
            '\t\t\t\t</div>\n',
            '\t\t\t</li>\n',
            '\t\t\t{% endwith %}\n',
            '\t\t</ul>\n',
            '\t</div>\n',
            '</nav>\n',
            '{% endblock sidebar %}\n',
            '\n',
        ])
        
        self.doc = a
    
    def set_file(self,path):
        """
        if not p.exists(path):
            template_file = open(path,"x")
            #self.__set_default_dependencies()
            
        else:
            template_file = open(path,"a")
            pass
        """
        return open(path,"x")
    
    def create(self, path="./result"):
        
        if not p.exists(path) :
            makedirs(path,0o777)
        
        path= path+"/nav.html"
            
        model_file = self.set_file(path)
        
        model_file.writelines(self.doc)
        pass
    pass

class Navs_Generator(object):
    def __init__(self,app, project_name, out_path):
        
        print("Cooking nav template ...")
        try:
            model_ = nav_generator(app, project_name)
            model_.create(path= out_path+project_name+"/Templates/layouts")
            
        except Exception as e:
            print(e)
        
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
    
    s=Navs_Generator(app,"project_test")