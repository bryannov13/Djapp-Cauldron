from os import path as p
from os import makedirs

class view_generator():
    
    def __init__(self, model_name):
        self.txt=[]
        self.fields=[]
        
        self.model_name = model_name
        self.form_name = self.model_name+"_form"
        
        self.list = []
        self.form = []
        self.delete = []
        
        self.__set_list()
        self.__set_form()
        self.__set_delete()
        
        
    
    def __set_default_dependencies(self):
        self.txt.append("from django.shortcuts import render\n")
        self.txt.append("from django.shortcuts import redirect\n")
        self.txt.append("from django.contrib import messages\n\n")#maybe this line will disapear
        
        self.txt.append("from ..models import "+self.model_name+" as item_model\n")
        self.txt.append("from ..forms import "+self.form_name+" as item_form\n")
        self.txt.append("\n")
    
    
    def __set_list(self):
        t=[]
        t.append("def _list(request):\n")
        t.append("\ttry:\n")
        t.append("\t\tquery = item_model.objects.all()\n")
        t.append("\t\tcontext = {'items_list' : query}\n")
        t.append("\t\tout = render(request,'./"+self.model_name+"/list.html',context)\n")
        
        t.append("\texcept:\n")
        t.append("\t\tmessages.error(request,'Something went wrong on showing list')\n")
        t.append("\t\tout = redirect('../')\n")
        
        t.append("\treturn out\n")
        t.append("\n")
        
        self.list = t
        
    def __set_form(self):
        t=[]
        t.append("def _form(request,id=None):\n")
        t.append("\tout = []\n")
        #start get method
        t.append("\tif request.method == 'GET':\n")
        t.append("\t\tif not id:\n")
        t.append("\t\t\tform = item_form()\n")
        
        t.append("\t\telse:\n")
        t.append("\t\t\titem = item_model.objects.get(pk=id)\n")
        t.append("\t\t\tform = item_form(instance=item)\n")
        
        t.append("\t\tout = render(request,'./"+self.model_name+"/form.html',{'form':form})\n")
        t.append("\n")
        #end get method
        
        #start post method
        t.append("\telif request.method == 'POST':\n")
        t.append("\t\tif not id:\n")
        t.append("\t\t\tform = item_form(request.POST)\n")
        
        t.append("\t\telse:\n")
        t.append("\t\t\ttry:\n")
        t.append("\t\t\t\titem = item_model.objects.get(pk = id)\n")
        t.append("\t\t\t\tform = item_form(request.POST,instance=item)\n")
        t.append("\t\t\texcept:\n")
        t.append("\t\t\t\tm = messages.error(request,'Something went wrong trying to get the item.')\n")
        
        t.append("\t\tif form.is_valid():\n")
        
        t.append("\t\t\ttry:\n")
        t.append("\t\t\t\tform.save()\n")
        t.append("\t\t\t\tm = messages.success(request, 'Item added sucessfull.')\n")
        t.append("\t\t\t\tout = redirect('"+self.model_name+"_list')\n")
        
        t.append("\t\t\texcept:\n")
        t.append("\t\t\t\tm = messages.error(request, 'Something went wrong on save.')\n")
        t.append("\t\t\t\tout = render(request,'./"+self.model_name+"/form.html',{'form':form,'messages':m})\n")
        
        t.append("\t\telse:\n")
        t.append("\t\t\tm=messages.error(request, 'Some fields with mistakes.')\n")
        t.append("\t\t\tout = render(request,'./"+self.model_name+"/form.html',{'form':form,'messages':m})\n")
        t.append("\n")
        
        #start except method
        t.append("\telse:\n")
        t.append("\t\tm = messages.error(request, 'Something went wrong verb action.')\n")
        t.append("\t\tout = render(request,'./"+self.model_name+"/list.html',{'messages':m})\n")
        
        t.append("\n")
        
        t.append("\treturn out\n")
        t.append("\n")
        
        
        self.form = t
        '''
        '''
    def __set_delete(self):
        t=[]
        t.append("def _delete(request,id):\n")
        t.append("\ttry:\n")
        t.append("\t\titem = item_model.objects.get(pk = id)\n")
        t.append("\t\titem.delete()\n")
        t.append("\t\tout = redirect('"+self.model_name+"_list')\n")
        
        t.append("\texcept:\n")
        t.append("\t\tout = redirect('/#')\n")
        
        t.append("\treturn out\n")
        t.append("\n")
        
        self.delete = t
        
    
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
            
            
        if not p.exists(path+"/__init__.py") :
            init_file = open(path+"/__init__.py", "x")
            init_file.close()
        
        path= path+"/"+self.model_name+"_view.py"
            
        model_file = self.set_file(path)
        
        #setting fuctions
        self.txt.extend(self.list)
        self.txt.extend(self.form)
        self.txt.extend(self.delete)
        
        
        self.txt.append("\n")

        model_file.writelines(self.txt)
        pass
    pass

class Views_Generator(object):
    def __init__(self,app,project_name,out_path):
        try:
            for m in app["tables"]:
                print("Cooking "+m["name"]+" view ...")
                model_ = view_generator(m["name"])
                model_.create(path= out_path+project_name+"/"+app["name"]+"/views")
                
        except Exception as e:
            print("Views:\n"+str(e))
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
    
    s=Views_Generator(app,"project_test")