from django import forms

from technical.models import UserAddress
from .models import Order


class OrderCreateForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Комментарий к заказу'}))
    address = forms.ModelChoiceField(label='', queryset=UserAddress.objects.all(), widget=forms.Select(attrs={'class': 'form-select w-50'}))

    class Meta:
        model = Order
        fields = ['address', 'comment']
