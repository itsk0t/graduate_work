from django.shortcuts import render
from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from cart.forms import CartAddProductForm
from products.models import Products, Category, Promotion


def product_list_view(request):
    form = CartAddProductForm()
    category = Category.objects.all()
    promotion = Promotion.objects.filter(~Q(id=1))
    products = Products.objects.filter(stop=True)
    return render(request, 'products/product_list.html',
                  {'products': products,
                   'promotion': promotion,
                   'category': category,
                    'form': form})


class ProductDetailView(FormMixin, DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product_detail'
    form_class = CartAddProductForm


class PromotionDetail(DetailView):
    model = Promotion
    template_name = 'products/promotion_detail.html'
    context_object_name = 'promotion'
