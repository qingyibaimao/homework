# coding=utf-8
from django.conf.urls import url
from . import views

app_name= 'comments'
urlpatterns= [
    url(r'^(?P<id>[0-9]+)/$', views.article_comment, name= 'article_comment'),
]