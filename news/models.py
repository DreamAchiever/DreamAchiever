# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type

class News(models.Model):
    '''新闻基本信息'''
    name = models.CharField(max_length=100)
    types = models.ManyToManyField(Type)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True)
#    create_person = models.ForeignKey(User)
    views = models.IntegerField()#查看次数
    source = models.CharField(max_length=20)#来源
    attachments = models.ManyToManyField(Media)
