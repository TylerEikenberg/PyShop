from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(req):
    products = Product.objects.all()
    return render(req, "index.html", {"products": products})


def new(req):
    return HttpResponse("New Products")
