from django.contrib import admin
from django.urls import path
from . views import user_create

urlpatterns = [
    path('login/',user_create,name='Login'),
    # path('success/',success_view,name='success'),
   
    
]
