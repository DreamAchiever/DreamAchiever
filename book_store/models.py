# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
    #单本书基本信息
    name = models.CharField(max_length=25)  #书名
    owner = models.CharField(max_length=10) #拥有者
    price = models.FloatField()             #书本标识价格
    book_type = models.IntegerField()       #对应BookType
    tag = models.ForeignKey()               #书标签
    recency = models.IntegerField()         #新旧程度
    ISBN = models.CharField(max_length = 25)#ISBN
    
    #借阅信息
    in_lib = models.BooleanField()          #是否在管
    in_time = models.DateTimeField()        #入管时间
    out_time = models.DateTimeField()       #出管时间
    borrow_time = models.DateTimeField()    #可借时间
    
    #出售信息
    sale_price = models.FloatField()        #出售价格   -1为不能出售
    sale_time = models.DateField()          #出售时间
    
class BookType(models.Model):
    #某书类基本信息
    name = models.CharField(max_length=25)  #书名
    author = models.CharField()             #作者名字
    press = models.CharField()              #出版社
    publish_time = models.DateField()       #出版日期
    lang = models.CharField(max_length=10)  #书语言
    page_count = models.IntegerField()      #书的页数
    type = models.CharField(max_lengyh=25)  #书的类型
    number = models.IntegerField()          #书的数量
    suit_to = models.CharField()            #适合人群
    
    #借阅信息
    borrow_count = models.IntegerField()    #借阅次数
    
    #出售信息
    sale_count = models.IntegerField()      #出售数量
    
    #评分信息
    score = models.FloatField()             #评分
    score_count = models.IntegerField()     #评分人数
    
class BorrowInf(models.Model):
    pass
class SaleInf(models.Model):
    pass
    
    