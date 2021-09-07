from django.contrib import admin

from .models import Category, Post, Comment


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','parent']

    class Meta:
        model=Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','description','post_image','category','stok','price']

    class Meta:
        model=Post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','yazar','text','created_time']
    list_filter = ['created_time']
    search_fields = ['text']

    class Meta:
        model=Comment

# Register your models here.
