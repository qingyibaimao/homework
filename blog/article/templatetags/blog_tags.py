# coding=utf-8
from ..models import Article
from django import template

register = template.Library()

@register.simple_tag
def get_recent_articles(num= 5):
    return Article.objects.all().order_by('-date_time')[:num]

@register.simple_tag
def archives():
    return Article.objects.dates('date_time', 'month', order='DESC')