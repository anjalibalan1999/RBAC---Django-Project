from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomLoginForm, PostForm
from .models import CustomUser, Post

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    user = request.user
    role = user.role

    if role == 0:  # Admin
        users = CustomUser.objects.all()
        posts = Post.objects.all()
        return render(request, 'admin_dashboard.html', {'users': users, 'posts': posts})

    elif role == 1:  # Moderator
        users = CustomUser.objects.all()
        return render(request, 'moderator_dashboard.html', {'users': users})

    else:  # User
        posts = Post.objects.all()
        return render(request, 'user_dashboard.html', {'posts': posts})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
