from django.db import models
from django import db
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, \
    PermissionsMixin


class Actor(models.Model):
    """ Models object"""
    name = models.CharField(max_length=255)
    parameters = models.OneToOneField('Parameters', on_delete=models.CASCADE)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE)


class Booker(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE, blank=True)
    # REQUIRED_FIELDS = ['username', 'schedule', 'first_name', 'last_name']
    # USERNAME_FIELD = 'email'
    #
    # def get_username(self):
    #     return  self.email


class Parameters(models.Model):
    sex = models.BinaryField()
    height = models.IntegerField()
    bust = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    shoe = models.IntegerField()
    hair = models.IntegerField()
    eyes = models.IntegerField()


class Schedule(models.Model):
    jobs = models.ManyToManyField('Job')


class Client(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE)


class Job(models.Model):
    models_id = models.ManyToManyField('Actor')
    client = models.ManyToManyField('Client')
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
