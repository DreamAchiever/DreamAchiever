# -*- coding: utf-8 -*-
from django.db import models
from authenticate.models import User
from util.models import Media,Type,Tag

class Personal(models.Model):
    '''个人活动'''
    name = models.CharField(max_length=20)#活动名称
    user = models.ForeignKey(User)#用户
    description = models.CharField(max_length=200)#活动描述
    begin_time = models.DateTimeField()#开始时间
    end_time = models.DateTimeField()#结束时间
    attachment = models.ManyToManyField(Media)#附件
    type = models.ManyToManyField(Type)#活动类型
    tag = models.ManyToManyField(Tag) #活动标签
    def __unicode__(self):
        return 'Personal:% ' % self.name