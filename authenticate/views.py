# Create your views here.
from django.http import HttpRequest,HttpResponse
from authenticate.models import User,Permission
from django.shortcuts import render_to_response
def login(req):
    req=HttpRequest()
    user=User.check(req['username'],req['password'])
    if user!=None:
        permissions= Permission.objects.filter(role__user__id=user.id)
        _login_(req,user,permissions)
        return {'success':True,'msg':'login success'}
    else:
        return {'success':False,'msg':'login failed'}
def logout(req):
    _logout_(req)
 
def _login_(req,user,permissions):
    req.session()
def _logout_(req):
    req.session().clear()
    req.flush()

def _get_user_(req):
    return req.session().get('')

def _get_permissions_(req):
    return req.session().get('')

def checkPermission(req):
    path=req.path
    permissions=_get_permissions_(req)
    for permission in permissions:
        if permission.url.equal(path):
            return True
    return False

def login_view(request):
#     return render_to_response('login.html')
    return HttpResponse("hello")

def search_path(path):
    start=0
    index=-1
    while True:
        k=index
        index=path.find("\\",start)
        if(index == -1):
            break
        start=index+1
    return k

def last_dir(path):
    index=search_path(path)
    str=path[0:index]
    str+="\\templates"
    return str