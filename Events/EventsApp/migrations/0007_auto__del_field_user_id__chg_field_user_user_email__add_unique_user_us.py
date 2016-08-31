# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.id'
        db.delete_column(u'EventsApp_user', u'id')


        # Changing field 'User.user_email'
        db.alter_column(u'EventsApp_user', 'user_email', self.gf('django.db.models.fields.EmailField')(max_length=75, primary_key=True))
        # Adding unique constraint on 'User', fields ['user_email']
        db.create_unique(u'EventsApp_user', ['user_email'])


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['user_email']
        db.delete_unique(u'EventsApp_user', ['user_email'])

        # Adding field 'User.id'
        db.add_column(u'EventsApp_user', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


        # Changing field 'User.user_email'
        db.alter_column(u'EventsApp_user', 'user_email', self.gf('django.db.models.fields.EmailField')(max_length=75))

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
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '30'}),
            'user_password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_phone': ('django.db.models.fields.BigIntegerField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['EventsApp']