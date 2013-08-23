from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
# Create your views here.
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if not request.POST.get('email',''):
            errors.append('Enter a email.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mial address')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                '454033517@qq.com',
                ['469370868@qq.com'],
                      )
            return HttpResponseRedirect('/contact/tanks/')
    return render_to_response('contact_form.html',{
        'errors':errors,
        'subject':request.POST.get('subject',''),
        'message':request.POST.get('message',''),
        'email':request.POST.get('email',''),                                                  
            },context_instance=RequestContext(request))
    
def handle_uploaded_file(f):
    destination = open('upload/'+f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    
def upload_file(request):
    if request.method == 'POST':
#         print form.is_valid()
#         if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect('/contact/tanks/')
    return render_to_response('upload_file.html')