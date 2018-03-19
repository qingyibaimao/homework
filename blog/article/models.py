from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User

#@python_2_unicode_compatible
#class Category(models.Model):


class Article(models.Model):
    title = models.CharField(max_length= 200)
    category = models.CharField(max_length= 100, blank= True)
    date_time = models.DateTimeField(auto_now_add= True)
    content = models.TextField(blank= True, null= True)
    excerpt = models.CharField(max_length=200, blank= True, null= True)
    author= models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'id': self.id})

   # def get_category():
   #     ret
    class Meta:
        ordering = ['-date_time']


