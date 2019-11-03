from django.db import models

class Bat(models.Model):
    name = models.ForeignKey(Question, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=200)
    probability = models.FloatField(default=0)
    image = models.CharField(max_length=1000)
