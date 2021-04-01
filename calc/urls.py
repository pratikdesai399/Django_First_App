from django.urls import path

from . import views

urlpatterns = [
    #Whenever you get a / i.e. home request use the home function from view.py
    path('',views.home, name='home')
]