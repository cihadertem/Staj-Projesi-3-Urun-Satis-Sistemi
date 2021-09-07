from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Başlık')
    description = models.TextField(blank=True,null=True,verbose_name='Açıklama')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Kategori')
    post_image = models.ImageField(null=True, blank=True, default='default_product.png',verbose_name='Resim')
    stok = models.IntegerField(verbose_name='Stok',default=0)
    kargo = models.IntegerField(null=True, blank=True,verbose_name="Kargo Ücreti", default=0)
    price = models.IntegerField(verbose_name='Fiyat',default="1")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

class Category(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True, related_name='categories')
    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
    yazar = models.ForeignKey('user.CustomUser', verbose_name='yazar', on_delete=models.CASCADE,related_name='posts')
    text = models.TextField(verbose_name='Yorum')
    created_time = models.DateTimeField(auto_now_add=True)
# Create your models here.
