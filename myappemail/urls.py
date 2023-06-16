from django.contrib import admin
from django.urls import path
from .views import contactView ,successView
from myappemail import views

urlpatterns = [
    path('',views.contactView,name='myappemail'),
    path("contact/", contactView,name="contact"),
    path("success/",successView,name="success"),

    
]