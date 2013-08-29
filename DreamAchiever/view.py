#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from authenticate.views import last_dir
import os
def hello(request):
    return HttpResponse("Hello world")


def contact_form(request):
    return render_to_response('calendar/contact_form.html')

def upload(request):
    path=os.path.join(last_dir(os.path.dirname(__file__)), 'calendar').replace('\\','/')
    return render_to_response('upload_file.html',{'path':path})