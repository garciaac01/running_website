# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Runner, Meet, Performance

# Register your models here.
admin.site.register(Runner)
admin.site.register(Meet)
admin.site.register(Performance)
