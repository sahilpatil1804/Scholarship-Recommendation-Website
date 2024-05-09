from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('filter_scholarships', views.filter_scholarships, name='filter_scholarships'),
]