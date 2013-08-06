# -*- coding: utf-8 -*-
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=255)
     
    def __unicode__(self):
        return "Tag:%s"%self.name

class Type(models.Model):
    name = models.CharField(max_length=20,unique=True)
    parent = models.ForeignKey('self',null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "Type:%s"%self.name

class Media(models.Model):
    name = models.CharField(max_length=20,unique=True)
    file_path = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    media_type = models.ForeignKey('MediaType')
    size = models.BigIntegerField()
    downloads = models.IntegerField()
#    create_person = models.ForeignKey(User)
    def __unicode__(self):
        return "Media:%s"%self.name
    
class MediaType(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.TextField()
    max_size = models.BigIntegerField()

class Option(models.Model):
    name = models.CharField(max_length=20,unique=True)
    value = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "Option:%s"%self.name

    
class FriendLink(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=255)
    url = models.URLField()
    display_order = models.IntegerField(default=0)
    logo = models.ForeignKey(Media)
    
    def __unicode__(self):
        return "FriendLink:%s"%self.name
    
class Announcement(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
#    target_roles = models.ManyToManyField(Role)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
#    create_person = models.ForeignKey(User)

    