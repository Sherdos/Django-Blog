from django.shortcuts import render, redirect
from post.models import Post, ProfileUser, Like, Comment, Following
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.
# MVT


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html',context)

def profile_user(request, id):
    following = Following.objects.filter(to_user_id = id, from_user_id = request.user.id)
    user = ProfileUser.objects.get(user_id=id)
    context = {
        'user':user,
        'following':following
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


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_config = request.POST.get('password_config')
        if username and password:
            if password == password_config:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                ProfileUser.objects.create(user_id=user.pk)
                login(request, user)
                return redirect('index')
            return render(request, 'error.html')
        return render(request, 'error.html')
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('index')

def edit_profile(request, id):
    user_profile = ProfileUser.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        user_profile.user.username = name
        user_profile.user.email = email
        user_profile.user.save()
        print(image)
        if image:
            user_profile.profile_image = image
            print('ff')
            user_profile.save()
        return redirect('profile_user', user_profile.user.pk)
    context = {
        'user':user_profile.user
    }
    return render(request, 'edit_profile.html', context)

def following(request):
    user_to = request.POST.get('user_to')
    try:
        Following.objects.get(to_user_id = user_to, from_user_id = request.user.id).delete()
    except:
        Following.objects.create(to_user_id = user_to, from_user_id = request.user.id)
    return redirect('profile_user', user_to)