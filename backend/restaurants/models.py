from django.db import models

class TypeCategory(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)

class LocationCategory(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)

class Restaurant(models.Model):
    def __str__(self):
        return self.store_name

    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    type = models.ForeignKey(TypeCategory, on_delete=models.CASCADE)
    location_type = models.ForeignKey(LocationCategory, on_delete=models.CASCADE)
    explain = models.CharField(max_length=500)
    latitude = models.FloatField(default=0.0) # 위도
    longitude = models.FloatField(default=0.0) # 경도
    store_image = models.ImageField(upload_to="media/restaurant", null=True)