from django.shortcuts import render
from .models import Post

def post_list(request):
    #query the database to get all the posts
    posts = Post.objects.all
    #Render the 'post_list.html' template, passing the 'posts'as a context variable
    return render(request, 'blog/post_list.html', {'posts': posts})