from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser): # username, password, email 은 기본 제공됨
    def __str__(self):
        return self.username 
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-\d{4}-\d{4}$")],
    )
    nickname = models.CharField(blank = True, max_length=20)