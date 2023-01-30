from django.urls import path

from app.views import index, ShopPage, contact, MenPage, WomenPage, login_view, register_view

urlpatterns = [
    path('', index, name='index'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('men/', MenPage.as_view(), name='men'),
    path('women/', WomenPage.as_view(), name='women'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register')
]
