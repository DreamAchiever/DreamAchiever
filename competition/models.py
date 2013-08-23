# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Type,Tag
# from authenticate.models import User

class Competition(models.Model):
    '''比赛基本类'''
    name = models.CharField(max_length=20,unique=True)#比赛名称
    description = models.CharField(max_length=200)#比赛描述
    begin_time = models.DateTimeField()#比赛开始时间
    end_time = models.DateTimeField()#比赛结束时间
    attachment = models.ManyToManyField(Media,related_name="competition")#比赛附件
    type = models.ManyToManyField(Type)
    tag = models.ManyToManyField(Tag)
#     create_person = models.ForeignKey(User)   
    cover = models.ForeignKey(Media,related_name="competition_cover")#封面图片
    def __unicode__(self):
        return 'Competition:% ' % self.name