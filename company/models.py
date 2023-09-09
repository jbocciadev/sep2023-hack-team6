from django.db import models


class Badges(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.CharField(max_length=200)


class MapData(models.Model):
    filename = models.CharField(max_length=200)
    latitute = models.FloatField()
    longitude = models.FloatField

    @property
    def coordinates(self):
        return [self.latitude, self.longitude]


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    badges = models.ManyToManyField(Badges)
    map_data = models.OneToOneField(MapData, on_delete=models.CASCADE)
