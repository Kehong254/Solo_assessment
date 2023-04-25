from django.db import models
from django.conf import settings
# Create your models here.

class Volcano(models.Model):
    Volcano_ID = models.IntegerField(primary_key=True)
    Volcano_Name = models.TextField(max_length=100)
    Volcano_Image = models.URLField(max_length=100)
    Volcano_Type = models.TextField(max_length=100)
    Country = models.TextField(max_length=100)
    epoch_period = models.TextField(max_length=100)
    Latitude = models.TextField()
    Longitude = models.TextField()

    def __str__(self):
        return f'{self.Volcano_ID},{self.Volcano_Name},{self.Volcano_Image},{self.Volcano_Type},{self.Country},{self.epoch_period},{self.Latitude},{self.Longitude}'
