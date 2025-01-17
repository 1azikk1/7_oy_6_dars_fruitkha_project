from django.shortcuts import render


def home(request):
    context = {
        'title': 'Fruitkha'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'about.html', context)


def error_404(request):
    context = {
        'title': 'Not Found'
    }
    return render(request, '404.html', context)


def cart(request):
    context = {
        'title': 'Cart'
    }
    return render(request, 'cart.html', context)


def news(request):
    context = {
        'title': 'News'
    }
    return render(request, 'news.html', context)


def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'contact.html', context)


def shop(request):
    context = {
        'title': 'Shop'
    }
    return render(request, 'shop.html', context)


def check_out(request):
    context = {
        'title': 'Checkout'
    }
    return render(request, 'checkout.html', context)


def product_detail(request):
    context = {
        'title': 'Single Product'
    }
    return render(request, 'single-product.html', context)


def news_detail(request):
    context = {
        'title': 'Single News'
    }
    return render(request, 'single-news.html', context)
