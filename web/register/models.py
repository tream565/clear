from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    account = models.EmailField(max_length = 254,unique=True)
    password = models.CharField(max_length=225)
    b_email = models.EmailField(max_length = 254,unique=True)



