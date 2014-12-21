"""
All awesome helpful functions go here.
"""

from random import randrange
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import urllib
import json
# import logging


def generate_random_string(chars=6):
    """Returns a random string of length `chars`"""
    return '%x'%randrange(16**chars)


def get_username_from_email(email=""):
    """Returns username from given email string"""
    if "@" in email:
        return email.split("@")[0]
    else:
        return email


def get_email_from_username(usernm=""):
    """Returns email from given username string"""
    if not "@" in usernm:
        return usernm + "@mu-sigma.com"
    else:
        return usernm


def send_pass_reset_mail(usernm="", valid_hash="", to="", reg=False):
    if usernm and valid_hash:
        if not to:
            to = get_email_from_username(usernm)
        url = "http://mukatta-anp.rhcloud.com/user/password_reset/{0}/{1}".format(usernm, valid_hash)
        if reg:
            title = "Registration successful!"
            message = "\n".join([
                'Hello & welcome to Mu Katta!',
                'Your registration was successful!',
                'Your username is %s'%usernm,
                'To login, you\'ll have to first reset your password.',
                'Goto this link to reset your password - %s'%url,
            ])
        else:
            title = "Password reset request"
            message = "\n".join([
                'Hello!',
                'Someone requested a password reset for your MuKatta account.',
                'Simply ignore this email if it wasn\'t you.',
                'Goto this link to reset your password - %s'%url,
            ])

        send_mail(
            'Mu Katta - %s'%title, message,
            settings.SERVER_EMAIL, [to,], fail_silently=False
        )
        return True


def reCaptcha(remote_ip="", captcha_response=""):
    """Utility for verifying a Google NoCaptchaReCaptcha"""

    SECRET = settings.NOCAPTCHA_SECRET
    VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": SECRET,
            "remoteip": remote_ip,
            "response": captcha_response}

    fetch_url = VERIFY_URL + "?secret={0}&response={1}&remoteip={2}".format(
        SECRET, captcha_response, remote_ip)
    response = urllib.urlopen(fetch_url)
    captcha_response = json.loads(response.read())
    if captcha_response["success"]:
        return True, "Success"
    else:
        if "error-codes" in captcha_response:
            return False, str(captcha_response["error-codes"])
        else:
            return False, "Unknown error"
