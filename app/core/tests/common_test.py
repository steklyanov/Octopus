from django.contrib.auth import get_user_model
from djoser.conf import settings as djoser_settings
from core.models import Actor, Agency, Booker

Token = djoser_settings.TOKEN_MODEL


def create_user(use_custom_data=False, **kwargs):
    data = (
        {"username": "john", "password": "secret", "email": "john@beatles.com"}
        if not use_custom_data
        else {
            "custom_username": "john",
            "password": "secret",
            "custom_email": "john@beatles.com",
            "custom_required_field": "42",
        }
    )
    data.update(kwargs)
    user = get_user_model().objects.create_user(**data)
    user.raw_password = data["password"]
    return user


def login_user(client, user):
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


def create_actor(name="ModelName", height=185, sex=1):
    actor = Actor()
    actor.name = name
    actor.height = height
    actor.sex = sex
    actor.save()
    return actor


def create_agency(name="AgencyName", address="AgencyAddress"):
    agency = Agency()
    agency.name = name
    agency.address = address
    agency.save()
    return agency


def create_booker(user):
    booker = Booker()
    booker.user = user
    booker.save()
    return booker


def create_agency_booker_model(user):
    """ Create user and booker from the same agency"""
    booker = create_booker(user)
    actor = create_actor()
    agency = create_agency()
    booker.agency = agency
    actor.agency = agency
    actor.save()
    booker.save()
    return booker, actor, agency
