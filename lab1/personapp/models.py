from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    work = models.CharField(max_length=30, default='')
    def __str__(self):
        return str(self.id)