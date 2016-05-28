from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='index'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    
)