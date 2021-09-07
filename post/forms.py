from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        fields = [

            'category',
            'title',
            'description',
            'post_image',
            'stok',
            'kargo',
            'price',

        ]
        model = Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [

            'text',

        ]

