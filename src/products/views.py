from django.http import Http404

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


# lista com produtos em destaque
class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()


# Pagina de detales dos produtos em destaque
class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"


# Lista todos os produtos do banco de dados sem filtro
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


# Detalhes dos produtos
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Não encontrado!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        return instance


class ProductDetailView(DetailView):

    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance
