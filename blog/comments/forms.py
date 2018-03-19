# coding=utf-8
from django import forms
from .models import Comment
from pagedown.widgets import AdminPagedownWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['name', 'email', 'text']

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(), required=False, label='')

