from django.db import models

# Create your models here.

class Url_Model(models.Model):
    URL = models.CharField(max_length=100)
