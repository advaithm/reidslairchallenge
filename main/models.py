from django.db import models
# Create your models here.
class tabel(models.Model):
    name = models.CharField(max_length = 10000000)
    status = models.CharField(max_length=1000)