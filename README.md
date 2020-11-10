# Djapp-Cauldron
Simple Django app builder from a json file
This tool helps to build a demo functional app with the CRUD basics
This is a django tool for build easily and fast web apps for Django

# Dependencies - Prepare the snacks 
    -Django 3.0.5
    -django-crispy-forms
    -django-dev-settings==2019.8.4

    $pip install -r req.txt

# My first food
inside the folder, run the next command
    $ py .\src\ 'json_path' './json_Examples/admin_products.json' './out/'

move to 
    './out/admin_products/'

setup your database
    './out/admin_products/admin_products/settings.py'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.<your Database>',
            'NAME': 'admin_products_django',
            'USER':'<your User>',
            'PASSWORD':'<your Password>',
            'HOST':'localhost'
        }
    }

Maybe you will need to install a django database dependencies, and change 'django.db.backends.<your Database>' to your database engine setup

it was tested with PostgreSQL


Make migrations and migrate
    $ py manage.py makemigrations
    $ py manage.py migrate

Run server
    $ py manage.py runserver

    then go to http://localhost:8000/app

# Input example

    {
        "name": "admin_products",
        "description": ":v",
        "databaseType": "PostgreSql",
        "tables": 
            [
                {
                    "name": "Producto_category",
                    "fields": [
                        {
                            "name": "Title",
                            "type": "String",
                            "required": "True",
                            "unique":"True"
                        }
                    ]
                },
                {
                    "name": "Product",
                    "fields": [
                        {
                            "name": "Title",
                            "type": "String",
                            "required": "True"
                        },
                        {
                            "name": "Category",
                            "type": "Producto_category",
                            "required": "True"
                        },
                        {
                            "name": "Stock",
                            "type": "Integer",
                            "required": "True"
                        }
                    ]
                }
            ]
    }

# Type of Data

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
        

On json_examples you will have some json examples, feel free to try or play with them 

On this version is not considered multiple apps, we are working on that

This is a collaboration with [Site Cauldron](http://sitecauldron.com)

# Arguments
    ################################
        Some arguments are required:
                argv[1] "json_path"|"json_string"
                argv[2] JSON path "./<yourJSONfile>.json" | string Your Json as string 
                argv[3] out_path "<yourOutput Path>"
    ################################

Any feature idea to make it better is welcome!!
