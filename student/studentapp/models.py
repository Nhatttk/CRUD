from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=55, null=False)
    age = models.IntegerField()
    image = models.ImageField(null=True)
    objects = models.Manager()


