from django.conf.urls import patterns, include, url
from mySite.views import current_datetime
from books import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$',current_datetime),
    (r'^admin/',include(admin.site.urls)),
    (r'^search-form/$',views.search_form),
    
    (r'^search/$',views.search),
    (r'^contact/$',views.contact),
)
