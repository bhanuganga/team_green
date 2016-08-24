
from django.db import models

class Event(models.Model):
        event_name=models.CharField(max_length=30)
        event_date=models.DateField()
        event_city=models.CharField(max_length=30)
        event_info=models.CharField(max_length=100)

class Cities(models.Model):
        city=models.CharField(primary_key=True,max_length=30)

        def __str__(self):
            return self.city