from django.db import models
# -*- coding: utf-8 -*-

# 主要目的是公共对外接口
class MailTask(models.Model):
    '''邮件任务'''
    #?我不太知道。附件是否可以发送
    name = models.CharField(max_length=20)  # 邮件标题
    happened_time = models.DateTimeField()  # 邮件发送时间
    content = models.TextField()  # 邮件内容
    MAIL_TYPE=(
               ('notice','日历提醒'),
               ('annoucement','公告系统'))
    mail_type = models.CharField(max_length=25,choices=MAIL_TYPE)
    mail_belong = models.IntegerField() #mail属于类型的id
    from_email = models.CharField(max_length=100) #发送者的email
    recipient_list = models.CharField(max_length=255) #目的地的email用逗号隔开xxx@xx.com,xx@xx.com
    complete = models.BooleanField()  # 是否已发送
