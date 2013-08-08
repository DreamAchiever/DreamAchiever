# -*- coding: utf-8 -*-
from django.db import models
from authenticate.models import User
from util.models import Media,Type,Tag
# Create your models here.
class Personal(models.Model):
    '''个人活动'''
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attachment = models.ManyToManyField(Media)
    type = models.ManyToManyField(Type)
    tag = models.ManyToManyField(Tag)  
    def __unicode__(self):
        return 'Personal:% ' % self.name