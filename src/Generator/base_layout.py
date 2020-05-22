from os import path as p
from os import makedirs

class base_generator():
    
    def __init__(self):
        self.doc = []
        self.__set_doc()
    
    def __set_doc(self):
        a=[
            '<!Doctype html>\n',
            '<html lang="en">\n',
            "\n",
            '\t<head>\n',
            '\t\t<!-- Required meta tags -->\n',
            '\t\t<meta charset="utf-8">\n',
            '\t\t<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n',
            "\n",
            '\t\t<title>{% block title %}Site Cauldron{% endblock title %}</title>\n',
            '\t</head>\n',
            '\t<body>\n',
            "\n",
            '\t\t{% include "./nav.html" %}\n',
            "\n",
            '\t\t<div class="container">\n',
            '\t\t\t<div class ="col-md-10 offset-md-1 mt-5">\n',
            '\t\t\t\t<div class="jumbotron">\n',
            '\t\t\t\t\t{% block content %}\n',
            "\n",
            '\t\t\t\t\t{% endblock content %}\n',
            '\t\t\t\t</div>\n',
            '\t\t\t</div>\n',
            '\t\t</div>\n',
            "\n",
            "\n",
            "\n",
            '\t\t{% include "./footer.html" %}\n',
            "\n",
            '\t\t<!-- Jquery -->\n',#May be jquery is not need it
            '\t\t<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>\n',
            "\n",
            
            '\t\t<!-- Bootstrap CSS -->\n',
            '\t\t<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>\n',
            '\t\t<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n',
            "\n",
            
            '\t\t<!-- Font Awsome -->\n',
            '\t\t<script src="https://kit.fontawesome.com/a076d05399.js"></script>\n',
            "\n",
            
            '\t\t<!-- jsdelivr -->\n', #maybe this line is not need it
            '\t\t<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\n',
            "\n",
            '\t</body>\n',
            '</html>\n',
            
        ]
        
        self.doc = a
    
    def set_file(self,path):
        return open(path,"x")
    
    def create(self, path="./result", default_fields=False):
        
        if not p.exists(path) :
            makedirs(path,0o777)
        
        path= path+"/base.html"
            
        model_file = self.set_file(path)
        
        model_file.writelines(self.doc)
        pass
    pass

class Base_template_generator(object):
    def __init__(self,app,project_name, out_path):
        print("Cooking base template ...")
        try:
            model_ = base_generator()
            model_.create(path= out_path+project_name+"/Templates/layouts")
            
        except Exception as e:
            print(e)
        


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
    
    s=Base_template_generator(app,"project_test")