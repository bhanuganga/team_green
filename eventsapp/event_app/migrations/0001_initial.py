# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cities'
        db.create_table(u'event_app_cities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'event_app', ['Cities'])

        # Adding model 'AddEvent'
        db.create_table(u'event_app_addevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_app.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'event_app', ['AddEvent'])

        # Adding model 'User'
        db.create_table(u'event_app_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=75, primary_key=True)),
            ('ph_no', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'event_app', ['User'])


    def backwards(self, orm):
        # Deleting model 'Cities'
        db.delete_table(u'event_app_cities')

        # Deleting model 'AddEvent'
        db.delete_table(u'event_app_addevent')

        # Deleting model 'User'
        db.delete_table(u'event_app_user')


    models = {
        u'event_app.addevent': {
            'Meta': {'object_name': 'AddEvent'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_app.User']"})
        },
        u'event_app.cities': {
            'Meta': {'object_name': 'Cities'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'event_app.user': {
            'Meta': {'object_name': 'User'},
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ph_no': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['event_app']