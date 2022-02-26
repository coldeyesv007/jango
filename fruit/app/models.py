from django.db import models

# Create your models here.
class student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    mark = models.IntegerField()
    image = models.FileField()