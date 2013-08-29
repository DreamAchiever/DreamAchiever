# -*- coding: utf-8 -*-
from django.db import models
from util.models import Media,Type,Tag
# Create your models here.

class Company(models.Model):
    '''公司基本信息'''
    name = models.CharField(max_length=20)#公司名称
    size = models.IntegerField()#略
    
    def __unicode__(self):
        return 'Company:% ' % self.name
    
    
class Work(models.Model):
    '''就业信息'''
    name = models.CharField(max_length=20)#就业职位信息
    company =models.ForeignKey(Company)#就业公司
    description = models.CharField(max_length=200)#就业描述
    begin_time = models.DateTimeField()#开始时间
    end_time = models.DateTimeField()#结束时间
    attachment = models.ManyToManyField(Media)#附件
    type = models.ManyToManyField(Type)#就业类型
    tag = models.ManyToManyField(Tag)#标签
    
    def __unicode__(self):
        return 'Work:% ' % self.name
    
