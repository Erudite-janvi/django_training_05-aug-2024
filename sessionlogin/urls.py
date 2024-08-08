from django.contrib import admin
from django.urls import path,include
from .views import login_view,logout_view,home_view
urlpatterns = [

    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('',home_view,name='home'),
    
]
