from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    (r'^$', 'index'),
    (r'^dept/(?P<page>\w+)/$', 'department'),

    (r'^community/$', 'community'),
    (r'^community/(?P<section>\w+)/$', 'community'),

    (r'^insurance/$', 'insurance'),
    (r'^directions/$', 'directions'),
    
    (r'^staff/(?P<section>\w+)/$', 'staff'),
    (r'^staff/(?P<section>\w+)/(?P<first>\w+)/(?P<last>\w+)/$', 'staff_bio'),

    (r'^contact/$', 'contact'),
    (r'^about/$', 'about'),



    # Example:
    # (r'^parkhealth/', include('parkhealth.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)

urlpatterns += patterns('', 
    (r'^admin/(.*)', admin.site.root), 
)
