# -*- coding: utf-8 -*-
from django.db import models
from authenticate.models import User
from personal.models import Personal
from work.models import Work
from competition.models import Competition 
from util.models import Media,Type,Tag

class Calendar(models.Model):
    '''日历'''
    name = models.CharField(max_length=20)
    calendar_type = models.CharField(max_length=20)
    work =models.ForeignKey(Work,null=True)
    competition = models.ForeignKey(Competition,null=True)
    personal = models.ForeignKey(Personal,null=True)
    create_time = models.DateTimeField()    
    def __unicode__(self):
        return 'Calendar:% ' % self.name

class Event(models.Model):
    '''事件'''
    name = models.CharField(max_length=30)
    calendar = models.ForeignKey(Calendar)
    description = models.CharField(max_length=200)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attachment = models.ManyToManyField(Media)
    type = models.ManyToManyField(Type)
    tag = models.ManyToManyField(Tag)  
    def __unicode__(self):
        return 'Event:%s' % self.name

class Notice(models.Model):
    '''提醒'''
    name = models.CharField(max_length=20)
    happened_time = models.DateTimeField()
    event = models.ForeignKey(Event)
    flag = models.IntegerField()
    def __unicode__(self):
        return 'Notice:% ' % self.name

class UserNoticeOption(models.Model):
    '''用户提醒设置'''
    name = models.CharField(max_length=20)
    notice = models.ForeignKey(Notice)
    def __unicode__(self):
        return 'UserNoticeOption:% ' % self.name
  
class Subscription(models.Model):
    '''订阅'''
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    calendar = models.ManyToManyField(User)
    def __unicode__(self):
        return 'Subscription:% ' % self.name





    
