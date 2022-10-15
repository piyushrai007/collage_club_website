from django.contrib import admin
from django.urls import path
from anonymous import views

urlpatterns = [
    path('',views.index,name='mysite'),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact"),

    
]

