from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='index'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_new"),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name="add_comment"),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name="comment_approve"),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name="comment_remove"),
)