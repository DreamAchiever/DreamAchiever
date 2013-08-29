# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type
from authenticate.models import User
class News(models.Model):
    '''新闻基本信息'''
    name = models.CharField(max_length=100)#新闻标题
    types = models.ManyToManyField(Type)#新闻类型
    tags = models.ManyToManyField(Tag)#新闻标签
    create_time = models.DateTimeField(auto_now_add=True)#创建时间
    create_person = models.ForeignKey(User)
    views = models.IntegerField()#查看次数
    source = models.CharField(max_length=20)#来源
    attachments = models.ManyToManyField(Media)#附件