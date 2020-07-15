from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        query = result.get('q', None)
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        else:
            return Product.objects.features()
