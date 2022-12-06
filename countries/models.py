from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser


class Country(models.Model):
    country_name = models.CharField(max_length=56)
    continent = models.CharField(max_length=56, default="")
    capital_city = models.CharField(max_length=56)
    flag_img = models.ImageField(upload_to='upload/', default="")
    time_zone = models.CharField(max_length=10)
    national_dish = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return reverse("detail_view", args=[self.id])
    
    class Meta:
        verbose_name_plural = "Countries"
