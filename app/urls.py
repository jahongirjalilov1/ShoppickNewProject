from django.urls import path

from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('men/', MenPage.as_view(), name='men'),
    path('women/', WomenPage.as_view(), name='women'),
    path('contact/', contact, name='contact'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('product-details/<int:product_id>', product_details, name='product-details'),
    path('about/', about, name='about'),
]
