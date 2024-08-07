from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # path('demo/',views.demo,name='demo'),
    path('users/',views.user_list,name= 'user_list'),
    path('users/<int:pk>/',views.user_detail,name = 'user_detail'),
    
    
]
