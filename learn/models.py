# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type,Comment
from authenticate.models import User
class Share(models.Model):
    '''学习共享'''
    name = models.CharField(max_length=20)
    description = models.TextField()
    types = models.ManyToManyField(Type)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True)
    create_person = models.ForeignKey(User)
    views = models.IntegerField()#查看次数
    attachments = models.ManyToManyField(Media)
    share_type = models.CharField(max_length=10)#学习资料，项目共享，你问我答
    
class ShareComent(Comment):
    '''分享评论'''
    