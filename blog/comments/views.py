from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article
from .models import Comment
from .forms import CommentForm

def article_comment(request, id):
    post = get_object_or_404(Article, id= id)
    if request.method == 'POST':
        form= CommentForm(request.POST)

        if form.is_valid():
            comment= form.save(commit= False)
            comment.article = post
            comment.save()
            return redirect(post)

        else:
            comment_list= post.comment_set.all()
            context= {'post': post,
                      'form': form,
                      'comment_list':comment_list
                      }
            return render(request, 'article/post.html', context= context)
    return redirect(post)
