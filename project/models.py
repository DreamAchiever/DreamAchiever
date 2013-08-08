# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type,Comment
from authenticate.models import User
class Project(models.Model):
    '''项目基本类'''
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    types = models.ManyToManyField(Type)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True)
    create_person = models.ForeignKey(User)
    charge_person = models.ForeignKey(User)
    join_persons = models.ManyToManyField(User,null=True)
    attachments = models.ManyToManyField(Media)
    views = models.IntegerField()
    comments = models.ManyToManyField('ProjectComment')

class ProjectComment(Comment):
    '''项目评论'''
    
    
