from django.db import models
from account.models import CustomUser
from django.contrib.auth import get_user_model
from django.conf import settings
# from .models import State

User = settings.AUTH_USER_MODEL 
# Create your models here.

class Cities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_city")
    city_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    popular = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.user)


class State(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_state")
    state_name = models.CharField(max_length=100)
    cm = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    cities = models.ManyToManyField(Cities)
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def cities_data(self):
        return ",".join([str(p) for p in self.cities.all()])

class Country(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_country")
    country_name = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField()
    pm = models.CharField(max_length=100)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return str(self.user)