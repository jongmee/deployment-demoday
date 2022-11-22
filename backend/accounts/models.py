from django.db import models

# Create your models here.

class Account(models.Model):
    def __str__(self):
        user_name = str(self.name)
        return user_name

    phone_number = models.IntegerField
    email = models.EmailField(max_length=30)
    id = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)