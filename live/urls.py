from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.index,name="m"),
    path('india/',views.india,name="k"),
path('about/',views.about,name="about"),
    path('about/suspect/',views.suspect,name="suspect")

]