from django.db.models.signals import post_save
from .models import Booker, Schedule
from django.contrib.auth import get_user_model


def create_booker(sender, instance, **kwargs):
    print("Heijhsadjf;psdfok")
    schedule = Schedule.objects.create()
    booker = Booker.objects.create(user=instance, schedule=schedule)


# def create_schedule(sender, instance, **kwargs):
#     print("sender = ", sender)
#     print("inst = ", instance)
#     print("create schedule")
#
#     instance.schedule = schedule


post_save.connect(create_booker, sender=get_user_model())
# post_save.connect(create_schedule, sender=Booker)
