from django.conf.urls import patterns, include, url

from django.contrib import admin

import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.time),
    url(r'^time/(\d{1,2})/$', views.hours_ahead),

)
