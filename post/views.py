from django.shortcuts import render
from post.models import Post
# Create your views here.
# MVT


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html',context)

def profile_user(request,id):
    return render(request, 'profile_user.html')

def detail_post(request, id):
    return(request, 'detail_post.html')


