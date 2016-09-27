# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hotel'
        db.create_table(u'hotel_app_hotel', (
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('Rent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hotel_app', ['Hotel'])

        # Adding model 'Booking'
        db.create_table(u'hotel_app_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Hotel_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hotel_app.Hotel'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
            ('Days', self.gf('django.db.models.fields.IntegerField')()),
            ('Persons', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('Total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hotel_app', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'Hotel'
        db.delete_table(u'hotel_app_hotel')

        # Deleting model 'Booking'
        db.delete_table(u'hotel_app_booking')


    models = {
        u'hotel_app.booking': {
            'Days': ('django.db.models.fields.IntegerField', [], {}),
            'Hotel_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotel_app.Hotel']"}),
            'Meta': {'object_name': 'Booking'},
            'Persons': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'Total': ('django.db.models.fields.IntegerField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        u'hotel_app.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'Rent': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['hotel_app']