# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Type,Tag
# Create your models here.

class Company(models.Model):
    '''公司基本信息'''
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    
    def __unicode__(self):
        return 'Company:% ' % self.name
    
    
class Work(models.Model):
    '''就业信息'''
    name = models.CharField(max_length=20)
    company =models.ForeignKey(Company)
    description = models.CharField(max_length=200)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attachment = models.ManyToManyField(Media)
    type = models.ManyToManyField(Type)
    tag = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return 'Work:% ' % self.name
    
