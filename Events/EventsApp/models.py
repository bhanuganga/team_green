from django.db import models

# Create your models here.


class Events(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    info = models.CharField(max_length=50)
    city = models.ForeignKey('Cities')

    def __unicode__(self):
        return u'{0}; DATE: {1}; CITY: {2};  DESC:{3}'.format(self.name, self.date, self.city, self.info)


class Cities(models.Model):
    place = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.place
