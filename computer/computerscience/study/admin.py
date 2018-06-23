# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from study.models import Year,Unit,Topics,Subtopics,News,Course
# Register your models here.

admin.site.register(Year)
admin.site.register(Topics)
admin.site.register(Subtopics)
admin.site.register(News)
admin.site.register(Unit)
admin.site.register(Course)