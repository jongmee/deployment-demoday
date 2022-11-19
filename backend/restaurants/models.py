from django.db import models


class Restaurant(models.Model):
    def __str__(self):
        return self.store_name
    TYPE_CHOICES = {
        ('한식', '한식'),
        ('중식', '중식'),
        ('양식', '양식'),
        ('일식', '일식')
    }
    LOCATION_CHOICES = {
        ('대흥', '대흥'),
        ('신촌', '신촌'),
        ('정문', '정문'),
        ('후문', '후문'),
        ('남문', '남문')
    }
    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    location_type = models.CharField(choices=LOCATION_CHOICES, max_length=20)
    explain = models.CharField(max_length=500)
    latitude = models.FloatField(default=0.0) # 위도
    longitude = models.FloatField(default=0.0) # 경도
    store_image = models.ImageField(upload_to="media/restaurant", null=True)