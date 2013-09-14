# -*- coding: utf-8 -*-
'''
Created on 2013-9-5

@author: 樊思勰

'''
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

#告看代码者：如果看不懂。则去查阅python装饰者函数
def url_deco(func=None,**kwargs):
	'''url优化装饰函数'''
	if func == None:		
		if kwargs['url'].startswith('/'):
			raise ValueError,"Custom URL can not begin with a '/'"
		url_deco.url = kwargs['url']
		return url_deco
	else :
		if hasattr(url_deco,'url'):
			func.url = url_deco.url
		else :
			func.url = func.__name__
		func.url_auto = True
		return func
	
#创建url映射，使用了python反射
class UrlMaker(object):
	@classmethod
	def build_url(cls,module,prefix=""):
		prefix = cls.check_prefix(prefix)
		url_patterns = []
		for member_name,module_member in module.__dict__.items():
			if hasattr(module_member,'url_auto') and module_member.url_auto:		
				url_patterns.append(url('^%s%s$' % (prefix,module_member.url), DreamAspect.method_invoke, {'method': module_member}))
		return url_patterns
	
	@staticmethod
	def check_prefix(prefix):
		'''检查前缀是否符合规则'''
		if prefix.endswith('/'):
			raise ValueError,"Custom prefix can not end with a '/'"
		if prefix.startswith('/'):
			raise ValueError,"Custom prefix can not start with a '/'"
		if prefix!="":
			prefix+="/"
		return prefix
	
class DreamAspect:
	'''用于切面开发'''
	@classmethod
	@csrf_exempt
	def method_invoke(cls,request,method=None):
		return method(request)
	