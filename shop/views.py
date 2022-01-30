from django.shortcuts import render
from shop.models import Product

# Create your views here.
def home(req):
    allProds={}
    cats = {obj['category'] for obj in Product.objects.values('category')}
    for cat in cats:
        prods = Product.objects.filter(category=cat).order_by('?')[:2]
        allProds[cat] = prods
    return render(req, 'shop/home.html', {'allProds':allProds})

def search(req):
    return render(req, 'shop/search.html')

def cart(req):
    return render(req, 'shop/cart.html')

def prodview(req, pid):
    pid = int(pid[8:])
    prod = Product.objects.get(id=pid)
    return render(req, 'shop/prodview.html', {'prod':prod})

def tracker(req):
    return render(req, 'shop/tracker.html')