from django.shortcuts import render, redirect
from post.models import Post
from cart.cart import Cart

def cart_add(request, id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.add(post=post)
    return redirect(url)

def item_clear(request, id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.remove(post)
    return redirect(url)#cart_detail yazılacak

def item_increment(request, id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.add(post=post)
    return redirect(url)#cart_detail yazılacak

def item_decrement(request, id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    post = Post.objects.get(id=id)
    cart.decrement(post=post)
    return redirect(url)#cart_detail yazılacak

def cart_clear(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    cart.clear()
    return redirect(url)#cart_detail yazılacak

def cart_detail(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    return render(request, 'cart_detail.html')


# Create your views here.
