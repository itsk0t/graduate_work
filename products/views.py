from django.shortcuts import render
from django.db.models import Q
from django.views.generic import DetailView
from products.models import Products, Category, Promotion


def product_list_view(request):
    category = Category.objects.all()
    promotion = Promotion.objects.filter(~Q(id=1))
    pizza = Products.objects.filter(category_id=1) & Products.objects.filter(stop=True)
    combo = Products.objects.filter(category_id=2) & Products.objects.filter(stop=True)
    return render(request, 'products/product_list.html',
                  {'combo': combo,
                   'pizza': pizza,
                   'promotion': promotion,
                   'category': category})


class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product_detail'
