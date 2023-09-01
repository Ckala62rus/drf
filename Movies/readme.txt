how to install new django project

1) Setting up a virtual enviroment
py -m venv project-name

2) Need run venv enviroment
project-name\Scripts\activate.bat

3) Next, you need install django
py -m pip install Django

4) create django project
django-admin startproject project-name

how to get all dependencies on virtual enviroment and write their to file
pip freeze > requirements.txt

delete all migration in module
./manage.py migrate my_app zero

delete migration on number igration
./manage.py migrate my_app 0010

show all migrations
python manage.py showmigrations


*******************
* DOCKER
*******************

1) вход в контейнер с питоном

   docker exec -ti django_rest /bin/bash

