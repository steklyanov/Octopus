from django.db import models
from django import db
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, \
    PermissionsMixin

User = get_user_model()


class Schedule(models.Model):
    jobs = models.ManyToManyField('Job', blank=True)


class Client(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE)


class Job(models.Model):
    models_id = models.ManyToManyField('Actor')
    client = models.ManyToManyField('Client')
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Agency(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Booker(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user


class Actor(models.Model):
    """ Models object"""
    EYE_COLOR = (('AMB', 'Amber'),
                 ('BLU', 'Blue'),
                 ('BRO', 'Brown'),
                 ('GRA', 'Gray'),
                 ('GRE', 'Green'),
                 ('HAZ', 'Hazel'))

    name = models.CharField(max_length=255)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, default=None)
    sex = models.BinaryField(null=True)
    height = models.IntegerField(null=True)
    bust = models.IntegerField(null=True)
    waist = models.IntegerField(null=True)
    hips = models.IntegerField(null=True)
    shoe = models.IntegerField(null=True)
    hair = models.IntegerField(null=True)
    eyes = models.CharField(max_length=3, choices=EYE_COLOR, null=True)

    def __str__(self):
        return self.name
