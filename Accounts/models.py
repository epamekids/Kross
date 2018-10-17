from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length = 20)
    firstname = models.TextField()
    lastname =  models.TextField()
