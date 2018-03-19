# coding=utf-8
from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'article'
urlpatterns =[
    url(r'^$', views.home, name= 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name= 'detail'),
    url(r'^test/$', views.test),
    url(r'^archives/$',views.archives, name='archives'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^tag/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'search/$', views.blog_search, name='search')

]
