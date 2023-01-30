from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages import INFO
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from app.forms import ProductModelForm, LoginForm, RegisterForm, send_email
from app.models import Product, Women, Men


def index(request):
    products = Product.objects.all()
    women = Women.objects.all()
    men = Men.objects.all()
    context = {
        'products': products,
        'women': women,
        'men': men
    }
    return render(request, 'app/index.html', context)


class ShopPage(ListView):
    template_name = 'app/shop.html'
    model = Product
    queryset = Product.objects.all().order_by()
    context_object_name = 'product'


class WomenPage(ListView):
    template_name = 'app/women.html'
    model = Women
    queryset = Women.objects.all().order_by()
    context_object_name = 'women'


class MenPage(ListView):
    template_name = 'app/men.html'
    model = Men
    queryset = Men.objects.all().order_by()
    context_object_name = 'men'

def contact(request):
    products = Product.objects.all()
    if request == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'products': products,
    }
    return render(request, 'app/contact.html', context)


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'app/auth/login.html', context)


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            send_email(form.data.get('email'), request, 'register')
            messages.add_message(
                request,
                level=messages.INFO,
                message='Xabar yuborildi, emailingizni tekshiring'
            )
            return redirect('register')
    context = {
        'form': form
    }
    return render(request, 'app/auth/register.html', context)




