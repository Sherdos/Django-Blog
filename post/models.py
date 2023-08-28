from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile', verbose_name='Пользователь')
    title = models.CharField(max_length=55, verbose_name='Название поста')
    description = models.TextField(verbose_name='Описание поста')
    image = models.ImageField(upload_to='post_image/', verbose_name='фото поста')
    created = models.DateTimeField(verbose_name='Дата пупликации поста', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
    def __str__(self) -> str:
        return f'{self.title} - {self.created}'

class ProfileUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_image = models.ImageField(upload_to='users/profile_image/', verbose_name='аватарка')
    
    class Meta:
        verbose_name = 'Профиль Пользователя'
        verbose_name_plural = 'Профиль Пользователей'
        
    def __str__(self) -> str:
        return f'{self.user}'


class Comment(models.Model):
    
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, verbose_name='Пост', related_name='comment_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='comment_user')
    text = models.TextField(verbose_name='Коментарий')
    
class Like(models.Model):
    
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, verbose_name='Пост', related_name='like_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='like_user')
    
    
class Following(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='user_to')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подпищик', related_name='user_from')