# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Titles

# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    #model = Titles
    pass

admin.site.register(Titles, TitleAdmin)