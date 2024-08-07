from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    file = models.FileField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.last_name