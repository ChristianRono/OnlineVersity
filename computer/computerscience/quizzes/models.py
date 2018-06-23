# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from study.models import Topics
# Create your models here.

class Question(models.Model):
	topic=models.ForeignKey(Topics)
	question=models.CharField(max_length=1000)
	
	def __unicode__(self):
		return self.question
		
class Multiple_choice(models.Model):
	question=models.ForeignKey(Question)
	choice=models.CharField(max_length=1000)
	
	def __unicode__(self):
		return self.choice
class Dummy(models.Model):
	pass

	
class Choice_answer(models.Model):
	choice=models.ForeignKey(Multiple_choice)
	explanation=models.TextField()
	
	def __unicode__(self):
		return self.choice
		
class Essay_answer(models.Model):
	question=models.ForeignKey(Question)
	answer=models.TextField()
	
	def __unicode(self):
		return self.question