# Djapp-Cauldron
Simple Django app builder from a json file
This tool helps to build a demo functional app with the CRUD basics
This is a django tool for build easily and fast web apps for Django

# Dependencies - Prepare the snacks 
    -Django 3.0.5
    -django-crispy-forms

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

#Input example

{
    "name": "admin_products",
    "description": ":v",
    "databaseType": "Postgresql",
    "tables": 
        [
            {
                "name": "Categoria_producto",
                "fields": [
                    {
                        "name": "Nombre",
                        "type": "String",
                        "required": "True",
                        "unique":"True"
                    }
                ]
            },
            {
                "name": "Producto",
                "fields": [
                    {
                        "name": "Nombre",
                        "type": "String",
                        "required": "True"
                    },
                    {
                        "name": "Categoria",
                        "type": "Categoria_producto",
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

On json_examples you will have some json examples, feel free to try or play with them 

On this version is not considered multiple apps, we are working on that

This is a collaboration with sitecauldron.com

Any feature idea to make it better is welcome!!
