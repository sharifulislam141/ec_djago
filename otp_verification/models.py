from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User
import random
import string

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def generate_otp(cls, user):
        otp = ''.join(random.choices(string.digits, k=6))
        otp_instance = cls(user=user, otp=otp)
        otp_instance.save()
        return otp

