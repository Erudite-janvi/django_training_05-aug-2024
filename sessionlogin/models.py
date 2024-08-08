from django.db import models

# Create your models here.
class Session(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    last_name = models.CharField(max_length=200,default='unkonwn')

    def __str__(self):
        return self.username + ' ' + self.email