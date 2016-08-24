from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=20)


class AddEvent(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    date = models.DateField()
    info = models.CharField(max_length=30)


