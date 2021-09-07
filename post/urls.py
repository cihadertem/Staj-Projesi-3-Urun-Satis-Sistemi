from django.urls import path
from .views import *
app_name='post'
urlpatterns = [
path('<int:id>', post_detail, name='detail'),
path('<int:id>/update', post_update, name='update'),
path('<int:id>/delete', post_delete, name='delete'),
path('create', post_create, name='create'),
path('category', category_view, name='category'),
path('category/<int:category_id>', category_index_view, name='category_index')
]