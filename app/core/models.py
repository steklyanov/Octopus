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

    def __str__(self):
        return self.name


class Job(models.Model):
    models_id = models.ManyToManyField('Actor')
    client = models.ManyToManyField('Client')
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None)

    def __str__(self):
        return 'Job for {}({})'.format(self.client, self.date)


class Agency(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Booker(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True, default=None, null=True)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}({})'.format(self.user, self.agency if self.agency else '')


class Actor(models.Model):
    """ Models object"""
    EYE_COLOR = (('AMB', 'Amber'),
                 ('BLU', 'Blue'),
                 ('BRO', 'Brown'),
                 ('GRA', 'Gray'),
                 ('GRE', 'Green'),
                 ('HAZ', 'Hazel'))

    HAIR_COLOR = (('BROWN', 'Brown'),
                  ('BLACK', 'Black'),
                  ('AUBUR', 'Auburn'),
                  ('RED', 'Red'),
                  ('WHITE', 'Grey or white'))

    name = models.CharField(max_length=255)
    schedule = models.OneToOneField('Schedule', on_delete=models.CASCADE, blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    bust = models.IntegerField(blank=True, null=True)
    waist = models.IntegerField(blank=True, null=True)
    hips = models.IntegerField(blank=True, null=True)
    shoe = models.IntegerField(blank=True, null=True)
    hair = models.CharField(max_length=5, choices=HAIR_COLOR, blank=True)
    eyes = models.CharField(max_length=3, choices=EYE_COLOR, blank=True)

    def __str__(self):
        return self.name
