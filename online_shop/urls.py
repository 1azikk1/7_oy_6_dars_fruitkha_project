from django.urls import path
from .views import home, about, error_404, cart, news, contact, shop, check_out, product_detail, news_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('error/404/', error_404, name='404'),
    path('cart/', cart, name='cart'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('checkout/', check_out, name='checkout'),
    path('product/detail/', product_detail, name='product_detail'),
    path('news/detail/', news_detail, name='news_detail'),
]
