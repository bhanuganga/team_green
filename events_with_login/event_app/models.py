
from django.db import models

class Event(models.Model):

        user = models.ForeignKey('Member', 'e_mail')
        event_name=models.CharField(max_length=30)
        event_date=models.DateField()
        event_city=models.CharField(max_length=30)
        event_info=models.CharField(max_length=100)

        def __unicode__(self):
                return u'NAME:{0};DATE:{1};CITY:{2};INFO:{3}'.format(self.event_name, self.event_date,self.event_city,self.event_info)

class Cities(models.Model):
        city=models.CharField(primary_key=True,max_length=30)

        def __str__(self):
            return self.city

class Member(models.Model):
        user_name=models.CharField(max_length=30)
        e_mail=models.EmailField(primary_key=True)
        password = models.CharField(max_length=15)
        mobile=models.CharField(max_length=11)

