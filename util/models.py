# -*- coding: utf-8 -*-
from django.db import models
from authenticate.models import User, Role

class Media(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 媒体名称
    file_path = models.CharField(max_length=255)  # 媒体路径
    description = models.CharField(max_length=255)  # 媒体描述
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    media_type = models.ForeignKey('MediaType')  # 媒体类型
    size = models.BigIntegerField()  # 文件大小
    downloads = models.IntegerField()  # 下载次数
    create_person = models.ForeignKey(User)  # 创建者
    def __unicode__(self):
        return "Media:%s" % self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 标签名称
    description = models.CharField(max_length=255)  # 标签注释
     
    def __unicode__(self):
        return "Tag:%s" % self.name

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 类型名称
    parent = models.ForeignKey('self', null=True)  # 父类型
    create_time = models.DateTimeField(auto_now_add=True)  # 创建类型
    description = models.CharField(max_length=255)  # 类型描述
    
    def __unicode__(self):
        return "Type:%s" % self.name
    
class MediaType(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 媒体类型名称
    description = models.TextField()  # 媒体类型描述
    max_size = models.BigIntegerField()  # 媒体上限大小
    def __unicode__(self):
        return 'MediaType:% ' % self.name

class Option(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 选项名称
    value = models.CharField(max_length=255)  # 选项值
    
    def __unicode__(self):
        return "Option:%s" % self.name
 
class FriendLink(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 友情链接名称
    description = models.CharField(max_length=255)  # 友情链接描述
    url = models.URLField()  # 友情链接URL
    display_order = models.IntegerField(default=0)  # 展现排序
    logo = models.ForeignKey(Media)  # 友情链接logo
    
    def __unicode__(self):
        return "FriendLink:%s" % self.name
    
class Announcement(models.Model):
    name = models.CharField(max_length=20)  # 公告名称
    content = models.TextField()  # 公告内容
    target_roles = models.ManyToManyField(Role)  # 公告面向角色
    ANNOUCEMENT_WAY = (
                     ('all', '所有方式'),
                     ('website', '站内'),
                     ('sms', '短信'),
                     ('mail', '邮件'))
    annoucement_way = models.CharField(max_length=10, choices=ANNOUCEMENT_WAY)  # 公告方式
    start_time = models.DateTimeField()  # 公告开始时间
    end_time = models.DateTimeField()  # 公告介绍时间
    create_person = models.ForeignKey(User)  # 创建人
    def __unicode__(self):
        return 'Announcement:% ' % self.name

class Comment(models.Model):
    content = models.TextField()  # 评论内容
    approve_num = models.IntegerField(default=0)  # 赞人数
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    
    def __unicode__(self):
        return 'Comment:% ' % self.approve_num
    class Meta:
        abstract = True
