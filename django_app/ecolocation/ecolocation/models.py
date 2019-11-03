from django.db import models
from django.urls import reverse
import datetime
import math

class Event(models.Model):
    name = models.CharField(max_length=100)
    
    lat = models.FloatField()
    lon = models.FloatField()
    
    start_time = models.DateField()
    end_time = models.DateField()

    num_joined = models.IntegerField(default=0)

    radius = models.FloatField()  # Miles


    def event_is_now(self):
        now = datetime.datetime.now()
        if now < self.end_time and now > self.start_time:
            return True
        return False

    def close_enough(self, lat2, lon2):
        lat1 = self.lat
        lon1 = self.lon
        R = 6371000
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
    
        deltaphi = math.radians(lat2 - lat1)
        deltalam = math.radians(lon2 - lon1)
    
        a = math.sin(deltaphi/2) * math.sin(deltaphi/2) + math.cos(phi1) * math.cos(phi2) * math.sin(deltalam/2) * math.sin(deltalam/2)
    
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
        d = R * c
    
        return d < self.radius

    def get_absolute_url(self):
        return reverse('modelforms:index')

    def is_valid(self):
        return True

    def __str__(self):
        print(f"{self.lat} {self.lon}")

