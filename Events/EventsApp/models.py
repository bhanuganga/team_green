from django.db import models

# Create your models here.


class Events(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    info = models.CharField(max_length=50)
    city = models.ForeignKey('Cities')


class Cities(models.Model):
    place = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.place
