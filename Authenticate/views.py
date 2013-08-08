# Create your views here.
from django.http import HttpRequest
from models import User,Permission
def login(req):
    req=HttpRequest()
    user=User.check(req['username'],req['password'])
    if user!=None:
        permissions= Permission.objects.filter(role__user__id=user.id)
        _login_(req,user,permissions)
        return {'success':True,'msg':'login success'}
    else:
        return {'success':False,'msg':'login failed'}
# def logout(req):
# 
def _login_(req,user,permissions):
    req.session()
def _logout_(req):
    req.flush()

# def _get_user_(req):
#     return req.session().get('')
# 
# def _get_permissions_(req):
#     return req.session().get('')
# def checkPermission(req):
#     path=req.path
#     permissions=_get_permissions_(req)
#     for permission in permissions:
#         if permission.url.equal(path):
#             return True
#     return False
# def add(req):
#     event=Event()
#     event.
#     

