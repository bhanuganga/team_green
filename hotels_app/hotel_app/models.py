from django.db import models

# Create your models here.
class Hotel(models.Model):
    Name=models.CharField(primary_key=True,max_length=20)
    Rent=models.IntegerField()

class Booking(models.Model):
    Hotel_name=models.ForeignKey('Hotel','Name')
    from_date=models.DateField()
    to_date=models.DateField()
    Days=models.IntegerField()
    Persons=models.IntegerField(max_length=5)
    Total=models.IntegerField()


