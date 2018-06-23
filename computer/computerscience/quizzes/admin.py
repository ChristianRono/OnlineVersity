# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from quizzes.models import Question,Multiple_choice,Choice_answer,Essay_answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Multiple_choice)
admin.site.register(Choice_answer)
admin.site.register(Essay_answer)