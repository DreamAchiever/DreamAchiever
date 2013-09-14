# -*- coding: utf-8 -*-
from core.dream_core import url_deco
from django.http.response import HttpResponse
from dream_calendar.models import Subscription

#获取当前用户的所有日历
@url_deco(url="sdfjksdlfl")
def get_calendars_by_login_user(request):
    login_user = request.session.get("login_user",None)
    if login_user :
        calendars = Subscription.objects.filter(user=login_user).order_by()
        
    return HttpResponse("1");
    