from django.urls import path, reverse_lazy

from products.views import product_list_view, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]