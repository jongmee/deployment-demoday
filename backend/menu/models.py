from django.db import models
from restaurants.models import Restaurant

class Sale(models.Model):
    def __str__(self):
        return self.sale_price

    sale_price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

class Menu(models.Model):
    def __str__(self):
        return self.menu_name

    menu_name = models.CharField(max_length=100)
    menu_price = models.IntegerField()
    menu_image = models.ImageField(upload_to="media/menu", null=True)

    sale = models.OneToOneField(Sale, on_delete=models.CASCADE, null = True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
