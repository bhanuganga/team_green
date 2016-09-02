from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=20)


class AddEvent(models.Model):
    user_info = models.ForeignKey('User', 'email_id' )
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    date = models.DateField()
    info = models.CharField(max_length=30)


class User(models.Model):
    username = models.CharField(max_length=20)
    email_id = models.EmailField(primary_key=True)
    ph_no = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)
