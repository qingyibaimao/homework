from django.shortcuts import render, get_object_or_404
from .models import Article
from datetime import datetime
from django.http import Http404
from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
  #  paginator = Paginator(posts, 2)  # 每页显示两个
  #  page = request.GET.get('page')
  #  try:
  #      post_list = paginator.page(page)
  #  except PageNotAnInteger:
  #      post_list = paginator.page(1)
  #  except EmptyPage:
  #      post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, id):
    post = get_object_or_404(Article, id= id)
    post.content = markdown.markdown(post.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'post.html', context= context)

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})

def about_me(request):
    post = get_object_or_404(Article, title='aboutme' )
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    return render(request, 'aboutme.html', {'post': post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                            'error' : False})

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request, 'archives.html', { 'post_list': post_list,
                                                          'error': True
                })
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')

