from os import path as p
from os import makedirs

class model_generator():
    
    def __init__(self, model_name):
        self.txt=[]
        self.fields=[]
        self.model_name = model_name
    
    
    def __set_default_dependencies(self):
        self.txt.append("from django.db import models \n")
        self.txt.append("from django.core.validators import MaxValueValidator, MinValueValidator \n")
        self.txt.append("\n")
    
    def set_fields(self,fields):
        for field in fields:
            f = "\t"+str(field["name"])+" = "
            
            type_ = field["type"]
            
            if type_ == 'String':
                t = "models.CharField(max_length=50)"
            elif type_ == 'Integer':
                t = "models.IntegerField()"
            elif type_ == 'Floating':
                t = "models.FloatField()"
            elif type_ == 'Boolean':
                t = "models.BooleanField()"
            elif type_ == 'DateTime':
                t = "models.DateField()"
                pass
            else:
                
                t = "models.ForeignKey("+str(type_)+", on_delete=models.CASCADE)"
                #print("please use: String, Integer, on "+f)
                pass
            self.fields.append(f+t+"\n")
            pass
    
    def __set_default_fields(self):
        self.txt.append("\n")
        self.txt.append("\tstatus = models.BooleanField(default=True)\n")
        self.txt.append("\tcreated_at = models.DateTimeField(auto_now_add=True)\n")
        self.txt.append("\tupdated_at = models.DateTimeField(auto_now=True)\n")
        pass
    
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
        path= path+"/models.py"
            
        model_file = self.set_file(path)
        
        self.txt.append("#"+str(self.model_name)+"_model \n")
        self.txt.append("class "+self.model_name+"(models.Model):\n")
        
        for field in self.fields:
            self.txt.append(field)
            
            pass
        
        if default_fields:
            self.__set_default_fields()
            
        self.txt.append("\n")

        model_file.writelines(self.txt)
        pass
    pass

class Models_Generator(object):
    def __init__(self,app,project_name,out_path):
        
        try:
            for m in app["tables"]:
                print("Cooking "+m["name"]+" model ...")            
                model_ = model_generator(m["name"])
                model_.set_fields(m["fields"])
                model_.create(path= out_path+project_name+"/"+app["name"],default_fields=True)
                pass
            
        except Exception as e:
            print("Models:\n")
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
    
    s=Models_Generator(app)