from django.urls import path
from .views import *
app_name='cart'
urlpatterns = [
path('<int:id>/addcart', cart_add, name='cartadd'),
path('item_clear/<int:id>/', item_clear, name='item_clear'),
path('item_increment/<int:id>/', item_increment, name='item_increment'),
path('item_decrement/<int:id>/', item_decrement, name='item_decrement'),
path('cart_clear/', cart_clear, name='cart_clear'),
path('cart-detail/',cart_detail,name='cart_detail'),
]