"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import index, profile_user, detail_post, create_post, add_like, add_comment, login_user, logout_user, register_user, following, edit_profile
from django.conf.urls.static import static
from Blog import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/<int:id>/', profile_user, name='profile_user'),
    path('posts/<int:id>/', detail_post, name='post'),
    path('posts/create', create_post, name='create_post'),
    path('posts/add/like', add_like, name='add_like'),
    path('posts/add/comment', add_comment, name='add_comment'),
    path('users/login', login_user, name='login_user'),
    path('users/logout', logout_user, name='logout_user'),
    path('users/register', register_user, name='register'),
    path('users/following', following, name='following'),
    path('users/edit/profile/<int:id>/', edit_profile, name='edit_profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)