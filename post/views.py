from django.shortcuts import render, redirect
from post.models import Post, ProfileUser, Like, Comment
from django.contrib.auth import login, authenticate, logout
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

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.POST.get('user_id')
        Post.objects.create(title = title, description = description, image=image, user_id = user)
        return redirect('index')
    return render(request, 'create_post.html')

def add_like(request):
    post = request.POST.get('post_id')
    user = request.POST.get('user_id')
    try:
        Like.objects.get(post=post, user=user).delete()
    except:
        Like.objects.create(post_id = post, user_id = user)
    return redirect('post', post)



def add_comment(request):
    post = request.POST.get('post_id')
    user = request.POST.get('user_id')
    text = request.POST.get('text')
    Comment.objects.create(post_id = post, user_id = user, text = text)
    return redirect('post', post)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')