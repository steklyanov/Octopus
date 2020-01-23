from django.contrib.auth import get_user_model
from djoser.conf import settings as djoser_settings

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
