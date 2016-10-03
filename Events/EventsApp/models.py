from django.db import models

# Create your models here.


class Events(models.Model):
    user = models.ForeignKey('User', 'user_email')
    name = models.CharField(max_length=20, blank=False)
    date = models.DateField(blank=False)
    info = models.CharField(max_length=50)
    city = models.ForeignKey('Cities', blank=False)

    def __unicode__(self):
        return u'{0}; DATE: {1}; CITY: {2};  INFO:{3}'.format(self.name, self.date, self.city, self.info)


class Cities(models.Model):
    place = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.place


class User(models.Model):
    user_name = models.CharField(max_length=30, blank=False, default=1)
    user_email = models.EmailField(primary_key=True, blank=False)
    user_phone = models.BigIntegerField(max_length=10, blank=False)
    user_password = models.CharField(max_length=20, blank=False)

    def __unicode__(self):
        return u'{0}:{1}'.format(self.user_name, self.user_email)
