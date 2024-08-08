from django.contrib import admin
from . models import Session
# Register your models here.

class SessionAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','email')
    search_fields = ('username', 'password','email')

admin.site.register(Session, SessionAdmin)