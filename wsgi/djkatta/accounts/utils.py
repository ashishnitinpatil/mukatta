"""
All awesome helpful functions go here.
"""

from random import randrange
from django.core.mail import send_mail
from django.conf import settings


def generate_random_string(chars=6):
    """Returns a random string of length `chars`"""
    return '%x'%randrange(16**chars)


def get_username_from_email(email=""):
    """Returns username from given email string"""
    if "@" in email:
        return email.split("@")[0]
    else:
        return ""


def get_email_from_username(usernm=""):
    """Returns email from given username string"""
    if not "@" in usernm:
        return usernm + "@mu-sigma.com"
    else:
        return ""


def send_reg_mail(to="", usernm="", passwd=""):
    if to and passwd:
        send_mail(
            'Mu Katta - Registration successful!',
            "\n".join([
                'Hello & welcome to Mu Katta!',
                'Your registration was successful.',
                'Your username is %s'%usernm,
                'Your password is %s'%passwd,
            ]),
            settings.SERVER_EMAIL,
            [to,],
            fail_silently=False
        )
        return True
