from django.urls import path
from newapp import views

# URL Configuration
urlpatterns = [
    path("", views.home, name="home"),
]