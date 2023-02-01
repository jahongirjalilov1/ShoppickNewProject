from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages import INFO
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from app.forms import ProductModelForm, send_email, CreateUserForm
from app.models import Product, Women, Men, Category


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
    paginate_by = 6

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return Product.objects.filter(title__icontains=title)
        return Product.objects.all()


class WomenPage(ListView):
    template_name = 'app/women.html'
    model = Women
    queryset = Women.objects.all().order_by()
    context_object_name = 'women'
    paginate_by = 6

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return Product.objects.filter(title__icontains=title)
        return Product.objects.all()


class MenPage(ListView):
    template_name = 'app/men.html'
    model = Men
    queryset = Men.objects.all().order_by()
    context_object_name = 'men'
    paginate_by = 6

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return Product.objects.filter(title__icontains=title)
        return Product.objects.all()

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

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)


def product_details(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'product': product,
        'products': products,
        'category': category
    }
    return render(request, 'app/product_detail.html', context)

def about(request):
    return render(request, 'app/auth/About.html')


def create_product(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ProductModelForm()
    context = {
        'form': form,
        'sizes': Product.ChoiceSize,
        'colors': Product.ChoiceColor,
        'price': Product.price,
        'categories': category
    }
    return render(request, 'app/create-product.html', context)



