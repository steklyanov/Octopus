from django.db.models.signals import post_save
from .models import Booker, Schedule
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def create_booker(sender, instance, **kwargs):
    print("Heijhsadjf;psdfok")
    schedule = Schedule.objects.create()
    booker = Booker.objects.create(user=instance, schedule=schedule)


def create_user(sender, instance, **kwargs):
    # user = User.objects.create()
    print("sender = ", sender)
    print("inst = ", instance)
    print("create schedule")

    # instance.schedule = schedule


post_save.connect(create_booker, sender=get_user_model())
post_save.connect(create_user, sender=Booker)
