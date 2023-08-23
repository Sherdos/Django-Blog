from django.contrib import admin
from post.models import Post, ProfileUser
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','created']
    list_display_links = ['id','title']
    search_fields = ['title', 'description']
    list_filter = ['created']
    
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['id','user']
    list_display_links = ['id','user']
    search_fields = ['user']

admin.site.register(Post,PostAdmin)
admin.site.register(ProfileUser,ProfileUserAdmin)