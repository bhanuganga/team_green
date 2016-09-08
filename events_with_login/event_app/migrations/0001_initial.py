# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'event_app_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_app.Member'])),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
            ('event_city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('event_info', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'event_app', ['Event'])

        # Adding model 'Cities'
        db.create_table(u'event_app_cities', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
        ))
        db.send_create_signal(u'event_app', ['Cities'])

        # Adding model 'Member'
        db.create_table(u'event_app_member', (
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('e_mail', self.gf('django.db.models.fields.EmailField')(max_length=75, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=11)),
        ))
        db.send_create_signal(u'event_app', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'event_app_event')

        # Deleting model 'Cities'
        db.delete_table(u'event_app_cities')

        # Deleting model 'Member'
        db.delete_table(u'event_app_member')


    models = {
        u'event_app.cities': {
            'Meta': {'object_name': 'Cities'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'})
        },
        u'event_app.event': {
            'Meta': {'object_name': 'Event'},
            'event_city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_info': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event_app.Member']"})
        },
        u'event_app.member': {
            'Meta': {'object_name': 'Member'},
            'e_mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['event_app']