from django.views.generic import ListView
from django.shortcuts import render

from .models import Product


class ProductListView(ListView):
    # lista todos os produtos do banco de dados (sem filtro)
    queryset = Product.objects.all()
    template_name = "products/list.html"
