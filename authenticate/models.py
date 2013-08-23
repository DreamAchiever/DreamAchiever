# -*- coding: utf-8 -*-
from django.db import models
from util import basemodels

class User(models.Model):
    '''用户登录信息'''
    user_name=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=50)
    create_time=models.DateTimeField()
    last_login_time=models.DateTimeField()
    email=models.EmailField()
    user_info = models.OneToOneField('UserInfo')
    def __unicode__(self):
        return 'User:% ' % self.user_name
    @classmethod
    def check(cls,username,password):
        users = User.objects.filter(user_name=username)
        if users[0].password == password:
            return users[0]
        return None
   
class Role(models.Model):
    '''角色'''
    role_name=models.CharField(max_length=30,unique=True)
    users=models.ManyToManyField(User)
    create_time=models.DateTimeField()
    def __unicode__(self):
        return 'Role:% ' % self.user_name
    
from util.models import Media
class UserInfo(models.Model):
    '''用户基本信息'''
    id = basemodels.UUIDField(primary_key=True)
    student_ID = models.CharField(max_length=30,null=True)
    grade = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    speciality = models.CharField(max_length=40,null=True)
    birthday=models.DateField(null=True)
    gender=models.CharField(max_length=10)
    interest=models.CharField(max_length=100,null=True)
    sphere = models.CharField(max_length=100,null=True)
    langue = models.CharField(max_length=30,null=True)
    describe = models.CharField(max_length=50,null=True)
    picture = models.ForeignKey(Media)
    def __unicode__(self):
        return 'UserInfo:% ' % self.user_name
    
    
class Permission(models.Model):
    '''权限'''
    url=models.URLField(unique=True)
    roles=models.ManyToManyField(Role)
    def __unicode__(self):
        return 'Permission:% ' % self.user_name