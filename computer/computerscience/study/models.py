# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime as dt

# Create your models here.
class Year(models.Model):
	name=models.CharField(max_length=20, unique=True)
	
	def __unicode__(self):
		return self.name

#class Semester(models.Model):
#    name=models.CharField(max_length=20, default=1)
#    
#    def __unicode__(self):
 #       return self.name

class Course(models.Model):
	name=models.CharField(max_length=1000)
	description=models.TextField()
	description_brief=models.CharField(max_length=1000)
	
	def __unicode__(self):
		return self.name
	
 
class Unit(models.Model):
	course=models.ForeignKey(Course)
	year=models.ForeignKey(Year)
	#semester=models.ForeignKey(Semester)
	name=models.CharField(max_length=1000, unique=True)
	description_brief=models.CharField(max_length=200)
	description=models.TextField()
	
	def __unicode__(self):
		return self.name
	
class Topics(models.Model):
	unit=models.ForeignKey(Unit)
	name=models.CharField(max_length=1000)
	number=models.IntegerField()
	
	def __unicode__(self):
		return self.name
		
class Subtopics(models.Model):
	topic=models.ForeignKey(Topics)
	name=models.CharField(max_length=1000)
	content=models.TextField()
	number=models.IntegerField()
	
	def __unicode__(self):
		return self.name

class News(models.Model):
	title=models.CharField(max_length=1000)
	content=models.TextField()
	date=models.DateField(default=dt.now)
	
	def __unicode__(self):
		return self.title