from django.db import models

# Create your models here.
class Bears(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    Bears = models.ForeignKey(Bears,on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.CharField(max_length=264, unique=True)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

class Users(models.Model):
    First_name=models.CharField(max_length=264, unique=True)
    Last_name=models.CharField(max_length=264, unique=True)
    Email=models.EmailField()
    def __str__(self):
        return str(self.First_name) + ' ' + str(self.Last_name)
