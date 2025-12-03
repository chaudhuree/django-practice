## install venv
``` 
pip  -m venv env
```
## activate venv
``` 
source env/Scripts/activate
```
## activate for mac
``` 
source env/bin/activate
```
---
### Using powershell
``` 
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Then run this command
```
env/Scripts/activate
```
---
## see all installed packages
``` 
pip freeze
```
## deactivate venv
``` 
deactivate
```
---
## create project
``` 
django-admin startproject project_name .
```

## run server
``` 
python manage.py runserver
```

## creating app
``` 
python manage.py startapp app_name
```

## super user
``` 
python manage.py createsuperuser
```

## change password
```
python manage.py changepassword <your_user_name>
```

## migrate
```
python manage.py makemigrations
python manage.py makemigrate
```

