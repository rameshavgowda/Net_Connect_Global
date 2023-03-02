

## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ Django-restframework
+ pandas
+ httpie
+ Jinja2
+ requests
+ Django
+ Git
+ pip
+ Virtualenv (virtualenvwrapper is recommended)

## Install Requirements

Run the below statements
```bash
> pip install -r requirements.txt
```

## Project Installation

To setup a local development environment:

+ For my convenience i create my database in sqLite for 
+ If you wish to change the database type to postgresql or mysql change the Database configuration in settings.py file
+ Perform the migration commands to create the table as bellow mentioned

```bash
    python manage.py makemigrations       
    python manage.py migrate  
```
## Project Running

+ Run the server

```bash
    python manage.py runserver  
```
+ click the bellow url to run the project 

http://127.0.0.1:8000/

