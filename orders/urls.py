from django.urls import path

from orders.views import order_create, OrderDelete

app_name = 'orders'

urlpatterns = [
    path('^create/', order_create, name='order_create'),
    path('<int:pk>/delete', OrderDelete.as_view(), name='order_delete'),
]

