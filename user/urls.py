from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('profile', profile_view, name='profile'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('edit',editprofile_view,name='edit'),
]