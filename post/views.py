from django.shortcuts import render
from post.models import Post, ProfileUser
# Create your views here.
# MVT


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html',context)

def profile_user(request, id):
    user = ProfileUser.objects.get(id=id)
    context = {
        'user':user
    }
    return render(request, 'profile_user.html', context)

def detail_post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'detail_post.html',context)


