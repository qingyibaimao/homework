from django.db import models
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Comment(models.Model):
    name= models.CharField(max_length= 100)
    email= models.EmailField(max_length= 200)
    url= models.URLField(blank= True)
    text= models.TextField()
    date_time= models.DateTimeField(auto_now_add= True)
    article= models.ForeignKey('article.Article', on_delete = models.CASCADE)

    def __str__(self):
        return self.text[:20]
