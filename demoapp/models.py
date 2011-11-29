from django.db import models
from django.contrib import admin

class Demo(models.Model):
    name = models.CharField(max_length=300)
    body = models.TextField()

admin.site.register(Demo)
