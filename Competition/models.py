# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media
from util.models import Media,Type,Tag
from authenticate.models  import User
# Create your models here.
class Competition(models.Model):
    '''比赛信息'''
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=200)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attachment = models.ManyToManyField(Media)
    type = models.ManyToManyField(Type)
    tag = models.ManyToManyField(Tag)
    create_person = models.ForeignKey(User)   
    media = models.ForeignKey(Media)
    def __unicode__(self):
        return 'Competition:% ' % self.name