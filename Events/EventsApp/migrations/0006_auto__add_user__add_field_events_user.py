# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'EventsApp_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(default=1, max_length=30)),
            ('user_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('user_phone', self.gf('django.db.models.fields.BigIntegerField')(max_length=10)),
            ('user_password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'EventsApp', ['User'])

        # Adding field 'Events.user'
        db.add_column(u'EventsApp_events', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['EventsApp.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'EventsApp_user')

        # Deleting field 'Events.user'
        db.delete_column(u'EventsApp_events', 'user_id')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['EventsApp.User']"})
        },
        u'EventsApp.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '30'}),
            'user_password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_phone': ('django.db.models.fields.BigIntegerField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['EventsApp']