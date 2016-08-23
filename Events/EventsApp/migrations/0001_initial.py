# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Events'
        db.create_table(u'EventsApp_events', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['EventsApp.Cities'])),
        ))
        db.send_create_signal(u'EventsApp', ['Events'])

        # Adding model 'Cities'
        db.create_table(u'EventsApp_cities', (
            ('place', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
        ))
        db.send_create_signal(u'EventsApp', ['Cities'])


    def backwards(self, orm):
        # Deleting model 'Events'
        db.delete_table(u'EventsApp_events')

        # Deleting model 'Cities'
        db.delete_table(u'EventsApp_cities')


    models = {
        u'EventsApp.cities': {
            'Meta': {'object_name': 'Cities'},
            'place': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        },
        u'EventsApp.events': {
            'Meta': {'object_name': 'Events'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['EventsApp.Cities']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['EventsApp']