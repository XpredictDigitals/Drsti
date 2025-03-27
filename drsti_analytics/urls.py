from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("add_complaint/", views.add_complaint, name="add_complaint"),
    path('view_complaints/', views.view_complaints, name='view_complaints'),




]