# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type,Comment
from authenticate.models import User
class Project(models.Model):
    '''项目基本类'''
    name = models.CharField(max_length=20)#项目名称
    description = models.CharField(max_length=255)#项目描述
    types = models.ManyToManyField(Type)#项目从属类型
    tags = models.ManyToManyField(Tag)#项目标签
    create_time = models.DateTimeField(auto_now_add=True)#创建时间
    create_person = models.ForeignKey(User,related_name="own_project")#创建人
    charge_person = models.ForeignKey(User,related_name="charge_project")#管理人
    join_persons = models.ManyToManyField(User,null=True)#报名参加人
    attachments = models.ManyToManyField(Media)#项目附件
    views = models.IntegerField()#查看次数

class ProjectComment(Comment):
    '''项目评论'''
    create_person = models.ForeignKey(User,related_name="own_comments")#创建人
    target_person = models.ForeignKey(User,null=True,related_name="targeted_comments")#朝向对象
    project = models.ForeignKey(Project)#从属项目
    
    
