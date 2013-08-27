# -*- coding: utf-8 -*-
from django.db import models
from authenticate.models import User
from util.models import Media, Type, Tag

class CalendarColor(models.Model):
    name = models.CharField(max_length=20)#配色方案名称
    content = models.CharField(max_length=255)#配色内容，逗号分隔如rgb(1,1,2),#FFF,rbga(2,3,4)
    
class Calendar(models.Model):
    '''日历'''
    name = models.CharField(max_length=20)  # 日历名称
    CALENDAR_TYPE=(
                   ('work','就业信息'),
                   ('competition','比赛信息'),
                   ('personal','个人信息'))
    calendar_type = models.CharField(max_length=20,choices=CALENDAR_TYPE)  # 日历类型
    belong_id = models.IntegerField() #日历从属类型的id
    create_time = models.DateTimeField(auto_now_add=True)  # 日历创建时间
    color = models.ForeignKey(CalendarColor) # 配色方案
    modify = models.CharField(max_length=10) # 日历性质 ：公开，私人
     
    def __unicode__(self):
        return 'Calendar:% ' % self.name

 
class Event(models.Model):
    '''事件'''
    name = models.CharField(max_length=30)  # 事件名称
    calendar = models.ForeignKey(Calendar)  # 事件属于的日历
    description = models.CharField(max_length=200)  # 事件内容
    begin_time = models.DateTimeField()  # 事件开始时间
    end_time = models.DateTimeField()  # 事件结束时间
    attachment = models.ManyToManyField(Media)  # 事件附件s
    type = models.ManyToManyField(Type)  # 事件类型
    tag = models.ManyToManyField(Tag)  # 事件标签
    EVENT_LEVEL = (
                 ('0',"普通"),
                 ('1',"紧急"),
                 ('2',"严重"),
                 )
    level = models.CharField(max_length=100,choices=EVENT_LEVEL,default="1")  # 事件等级
    
    def __unicode__(self):
        return 'Event:%s' % self.name
 
class Notice(models.Model):
    '''提醒'''
    #提醒这边还有点模糊，主要是订阅那个提前提醒时间的问题啊
    notice_period = models.IntegerField(default=0)  # 提前提醒时间
    time_unit = models.CharField(max_length=5)  # 分钟，小时，天，周，月
    event = models.ForeignKey(Event)  # 提醒从属事件   
    notice_type = models.CharField(max_length=10)  # 提醒方式mail,sms
    person = models.ForeignKey(User)  # 提醒对象
     
    def __unicode__(self):
        return 'Notice:% ' % self.name
   
class Subscription(models.Model):
    '''订阅'''
    name = models.CharField(max_length=20)  # 订阅名称
    user = models.ForeignKey(User)  # 订阅人
    calendar = models.ForeignKey(Calendar)  # 订阅日历

     
    def __unicode__(self):
        return 'Subscription:% ' % self.name
 
 
 
 
 
     
