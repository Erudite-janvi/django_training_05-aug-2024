from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
     list_display = ('name','last_name','email')

     search_fields = ('name','last_name','email')

admin.site.register(User,UserAdmin)