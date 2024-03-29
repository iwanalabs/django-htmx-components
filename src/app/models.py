from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=100, default="Inactive")


class Job(models.Model):
    progress = models.IntegerField(default=0)


class Brand(models.Model):
    name = models.CharField(max_length=100)


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
