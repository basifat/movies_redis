# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Titles(models.Model):

    title = models.CharField(max_length=255)
    overview =  models.TextField(null=True, blank=True)
    vote_average = models.IntegerField(default=0)
    #new = models.CharField(max_length=30)

    class Meta(object):
        app_label = 'titles'
        #default_related_name = 'app'

    def __unicode__(self):
        return self.title