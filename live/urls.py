from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.index,name="m"),
    path('india/',views.india,name="k"),
path('about/',views.about,name="about"),
    path('about/suspect/',views.suspect,name="suspect"),
    path('worlddata/',views.countryall.as_view(),name="api1"),
path('indiadata/',views.stateall.as_view(),name="api2"),
path('districtdata/',views.districtall.as_view(),name="api3"),
path('countrydata/<str:pk>/',views.country.as_view(),name="api4"),
path('statedata/<str:pk>/',views.state.as_view(),name="api5"),
path('districtdata/<str:pk>/',views.district.as_view(),name="api6"),
path('worldhead/',views.headworld.as_view(),name="api"),
path('indiahead/',views.headindia.as_view(),name="api"),

]