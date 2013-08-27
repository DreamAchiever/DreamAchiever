# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type,Comment
from authenticate.models import User
class Share(models.Model):
    '''学习共享'''
    name = models.CharField(max_length=20)#共享名称
    description = models.TextField()#描述信息
    types = models.ManyToManyField(Type)#共享类型
    tags = models.ManyToManyField(Tag)#共享标签
    create_time = models.DateTimeField(auto_now_add=True)#创建时间
    create_person = models.ForeignKey(User)#创建人
    views = models.IntegerField()#查看次数
    attachments = models.ManyToManyField(Media)#附件
    share_type = models.CharField(max_length=10)#学习资料，项目共享，你问我答
    
class ShareComment(Comment):
    '''分享评论'''
    create_person = models.ForeignKey(User,related_name="create_share_comment")#创建评论人
    target_person = models.ForeignKey(User,related_name="target_share_comment")#评论朝向对象