
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.loginpage,name='login'),
    path('home/',views.homepage,name='homepage'),
    path('register/',views.registration,name='register'),
    path('logout/',views.logoutpage,name='logout')
]
