from .forms import LoginForm, RegisterForm, ProfileUpdateForm
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def editprofile_view(request):
    user = request.user
    form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('user:profile')

    return render(request, "user/form.html", {"form": form, 'title': 'Profili Düzenle'})
    def get_object(self):
        return self.request.user

def profile_view(request):
    if not request.user.is_authenticated:
        raise Http404()
    return render(request, 'user/profile.html')

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')

    return render(request, "user/form.html", {"form": form, 'title': 'Üye Ol'})

def login_view(request):
    if request.user.is_authenticated:
        raise Http404()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, "user/form.html", {"form": form, 'title': 'Giriş Yap'})

def logout_view(request):
    if not request.user.is_authenticated:
        raise Http404()
    logout(request)
    return redirect('home')

def user_profile_view(request,username):
    user=get_object_or_404(CustomUser,username=username)
    return render(request, 'user/userprofile.html', {'user': user})
# Create your views here.
