from django.shortcuts import render
from .models import User, Post, Comment, Category


def index(request):
    return render(request, 'blog/index.html')


def base(request):
    return render(request, 'blog/base.html')


def users(request):
    users_list = User.objects.all()
    return render(request, 'blog/users.html', {'users': users_list})



def blogs(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts_list})


def comments(request):
    comments_list = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments_list})


def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories_list})


def blogdetails(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/blogdetails.html', {'post': post})
