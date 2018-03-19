from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from article import views
from article import urls as urll
urlpatterns = [
    path('article/', include('article.urls')),
   #  url('^$', views.home, name= 'home'),
    path('admin/', admin.site.urls),
    url(r'comment/', include('comments.urls'))

]
