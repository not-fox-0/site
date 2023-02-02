from django.shortcuts import render, redirect
from .models import Product, Comments
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as log_in, logout




def index(request):
    prd = Product.objects.all()
    return render(request, 'devise/index.html', {'prd': prd})


def product_view(request, slug):
    comm = ''
    if request.method == 'POST':
        comment = request.POST.get('comment')
        comm = Product.objects.get(slug=slug)
        comm.comments_set.create(username=request.user.username, comment=comment)

    prd = Product.objects.get(slug=slug)
    c = prd.comments_set.all()
    return render(request, 'devise/product.html', {'prd': prd, 'comm': c})


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            redirect('signin')
            form.save()

    return render(request, 'devise/register.html', {'form': form})


def login(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_in(request, user)
            redirect('home')

    return render(request, 'devise/signin.html')


def logoutUser(request):
    logout(request)
    return redirect('signin')

    