from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path('Selection-page/', views.selection, name='selection'),
    path('', views.selection, name='selection'),


]