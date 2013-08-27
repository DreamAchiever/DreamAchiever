# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Tag,Type,Comment
from authenticate.models import User
class Blog(models.Model):
    '''博客基本信息'''
    name = models.CharField(max_length=100)#博客文章名称
    types = models.ManyToManyField(Type)#博客分类
    tags = models.ManyToManyField(Tag)#博客标签
    create_time = models.DateTimeField(auto_now_add=True)#博客创建时间
    create_person = models.ForeignKey(User)#博客创建人
    views = models.IntegerField()#查看次数
    source = models.CharField(max_length=20)#来源
    attachments = models.ManyToManyField(Media)#博客附件
     
class BlogComment(Comment):
    '''博客评论'''
    create_person = models.ForeignKey(User,related_name="create_blog_comment")#创建评论人
    target_person = models.ForeignKey(User,related_name="target_blog_comment")#评论朝向对象