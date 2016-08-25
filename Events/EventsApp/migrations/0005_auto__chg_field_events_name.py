# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Events.name'
        db.alter_column(u'EventsApp_events', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'Events.name'
        db.alter_column(u'EventsApp_events', 'name', self.gf('django.db.models.fields.IntegerField')(max_length=20))

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