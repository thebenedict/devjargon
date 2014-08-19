from django.conf.urls import patterns, include, url
from django.contrib import admin
from detect.views import DocumentView, DocumentListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devjargon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^documents/$', DocumentListView.as_view(), name='document-list'),
    url(r'^documents/(?P<pk>\d+)/$', DocumentView.as_view(), name='document'),
)
