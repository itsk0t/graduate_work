from django.shortcuts import render, redirect

from account.forms import UserAddressForm
from orders.models import Order, OrderItem
from technical.models import UserAddress


def account_view(request):
    order = Order.objects.filter(user_id=request.user)
    order_item = OrderItem.objects.all()
    user_address = UserAddress.objects.filter(user_id=request.user)
    form = UserAddressForm(request.POST)
    if form.is_valid():
        account = form.save(commit=False)
        account.user_id = request.user
        account.save()

        return redirect('account:account')

    else:
        form = UserAddressForm

    return render(request, 'account/account.html', {'form': form, 'user_address': user_address, 'order': order, 'order_item': order_item})
