from django.conf.urls import patterns, include, url
from authenticate.views import login,login_view
from DreamAchiever.view import hello
from util.views import contact,upload_file
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MakeDream.views.home', name='home'),
    # url(r'^MakeDream/', include('MakeDream.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',hello),
#     (r'^contact-form/$',contact_form),
    (r'^contact/$',contact),
#     (r'^contact/tanks/$',thanks),
#     (r'^upload/$',upload),
    (r'^upload_file/$',upload_file),

 
)
