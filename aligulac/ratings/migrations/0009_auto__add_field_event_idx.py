# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.idx'
        db.add_column('event', 'idx',
                      self.gf('django.db.models.fields.IntegerField')(db_index=True, default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.idx'
        db.delete_column('event', 'idx')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ratings.alias': {
            'Meta': {'db_table': "'alias'", 'object_name': 'Alias'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Player']"})
        },
        'ratings.balanceentry': {
            'Meta': {'db_table': "'balanceentry'", 'object_name': 'BalanceEntry'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_gains': ('django.db.models.fields.FloatField', [], {}),
            'pvt_losses': ('django.db.models.fields.IntegerField', [], {}),
            'pvt_wins': ('django.db.models.fields.IntegerField', [], {}),
            'pvz_losses': ('django.db.models.fields.IntegerField', [], {}),
            'pvz_wins': ('django.db.models.fields.IntegerField', [], {}),
            't_gains': ('django.db.models.fields.FloatField', [], {}),
            'tvz_losses': ('django.db.models.fields.IntegerField', [], {}),
            'tvz_wins': ('django.db.models.fields.IntegerField', [], {}),
            'z_gains': ('django.db.models.fields.FloatField', [], {})
        },
        'ratings.earnings': {
            'Meta': {'db_table': "'earnings'", 'object_name': 'Earnings'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'earnings': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origearnings': ('django.db.models.fields.IntegerField', [], {}),
            'placement': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"})
        },
        'ratings.event': {
            'Meta': {'object_name': 'Event', 'db_table': "'event'", 'ordering': "['lft', 'latest', 'fullname']"},
            'big': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'earliest': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'family': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['ratings.EventAdjacency']", 'to': "orm['ratings.Event']", 'symmetrical': 'False'}),
            'fullname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'homepage': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idx': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'default': '0'}),
            'latest': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'noprint': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_event'", 'null': 'True', 'blank': 'True', 'to': "orm['ratings.Event']"}),
            'prizepool': ('django.db.models.fields.NullBooleanField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'rgt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'tl_thread': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tlpd_db': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tlpd_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'})
        },
        'ratings.eventadjacency': {
            'Meta': {'db_table': "'eventadjacency'", 'object_name': 'EventAdjacency'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uplink'", 'to': "orm['ratings.Event']"}),
            'distance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downlink'", 'to': "orm['ratings.Event']"})
        },
        'ratings.group': {
            'Meta': {'db_table': "'group'", 'object_name': 'Group'},
            'active': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'disbanded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'founded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'meanrating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '0.0'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['ratings.GroupMembership']", 'to': "orm['ratings.Player']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'scoreak': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '0.0'}),
            'scorepl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '0.0'}),
            'shortname': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '25'})
        },
        'ratings.groupmembership': {
            'Meta': {'db_table': "'groupmembership'", 'object_name': 'GroupMembership'},
            'current': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'playing': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'ratings.match': {
            'Meta': {'db_table': "'match'", 'object_name': 'Match'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '200'}),
            'eventobj': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['ratings.Event']"}),
            'game': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'default': "'WoL'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Period']"}),
            'pla': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_pla'", 'to': "orm['ratings.Player']"}),
            'plb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_plb'", 'to': "orm['ratings.Player']"}),
            'rca': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1'}),
            'rcb': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1'}),
            'rta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rta'", 'null': 'True', 'to': "orm['ratings.Rating']"}),
            'rtb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rtb'", 'null': 'True', 'to': "orm['ratings.Rating']"}),
            'sca': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'scb': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'treated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ratings.message': {
            'Meta': {'db_table': "'message'", 'object_name': 'Message'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Event']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Player']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'ratings.period': {
            'Meta': {'db_table': "'period'", 'object_name': 'Period'},
            'computed': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'dom_p': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dom_t': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dom_z': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_recompute': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'num_games': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_newplayers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_retplayers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        },
        'ratings.player': {
            'Meta': {'object_name': 'Player', 'db_table': "'player'", 'ordering': "['tag']"},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'dom_end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_dom_end'", 'null': 'True', 'blank': 'True', 'to': "orm['ratings.Period']"}),
            'dom_start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_dom_start'", 'null': 'True', 'blank': 'True', 'to': "orm['ratings.Period']"}),
            'dom_val': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'mcnum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1'}),
            'sc2c_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sc2e_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30'}),
            'tlpd_db': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tlpd_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'ratings.prematch': {
            'Meta': {'db_table': "'prematch'", 'object_name': 'PreMatch'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.PreMatchGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pla': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prematch_pla'", 'null': 'True', 'blank': 'True', 'to': "orm['ratings.Player']"}),
            'pla_string': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "''", 'max_length': '200'}),
            'plb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prematch_plb'", 'null': 'True', 'blank': 'True', 'to': "orm['ratings.Player']"}),
            'plb_string': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "''", 'max_length': '200'}),
            'rca': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1'}),
            'rcb': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1'}),
            'sca': ('django.db.models.fields.SmallIntegerField', [], {}),
            'scb': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'ratings.prematchgroup': {
            'Meta': {'db_table': "'prematchgroup'", 'object_name': 'PreMatchGroup'},
            'contact': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "''", 'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '200'}),
            'game': ('django.db.models.fields.CharField', [], {'default': "'wol'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': "''"}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "''", 'max_length': '500'})
        },
        'ratings.rating': {
            'Meta': {'object_name': 'Rating', 'db_table': "'rating'", 'ordering': "['period']"},
            'bf_dev': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
            'bf_dev_vp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
            'bf_dev_vt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
            'bf_dev_vz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
            'bf_rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vp': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vt': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vz': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'comp_rat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat_vp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat_vt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat_vz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'decay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dev': ('django.db.models.fields.FloatField', [], {}),
            'dev_vp': ('django.db.models.fields.FloatField', [], {}),
            'dev_vt': ('django.db.models.fields.FloatField', [], {}),
            'dev_vz': ('django.db.models.fields.FloatField', [], {}),
            'domination': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Period']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vp': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vt': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vz': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'prev': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prevrating'", 'null': 'True', 'to': "orm['ratings.Rating']"}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'rating_vp': ('django.db.models.fields.FloatField', [], {}),
            'rating_vt': ('django.db.models.fields.FloatField', [], {}),
            'rating_vz': ('django.db.models.fields.FloatField', [], {})
        },
        'ratings.story': {
            'Meta': {'db_table': "'story'", 'object_name': 'Story'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ratings']