# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type

class Project(models.Model):
    '''项目基本类'''
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    types = models.ManyToManyField(Type)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True)
#    create_person = models.ForeignKey(User)
#    charge_person = models.ForeignKey(User)
#    join_persons = models.ManyToManyField(User,null=True)
    attachments = models.ManyToManyField(Media)
    views = models.IntegerField()
    comments = models.ManyToManyField('ProjectComment')

class ProjectComment(models.Model):
    '''项目评论'''
    content = models.TextField()
#    create_person = models.ForeignKey(User)
#    target_person = models.ForeignKey(User,null=True)
    approve_num =models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    
