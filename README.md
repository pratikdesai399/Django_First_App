# Django_First_App
STEPS TO RUN THE APP :

1. cd into the directory
2. run python manage.py runserver


STEPS DONE:

1. django-admin startproject project_name
2. cd into the project
3. Made a calc app with command python manage.py startapp calc
4. cd into calc and made a file urls.py to basically add functionality
5. Made changes to views.py in calc to add a function home to display Hello message
6. Finally made changes to urls.py in main project folder to tell it that whenever you get a home request look for it in urls.py of calc
