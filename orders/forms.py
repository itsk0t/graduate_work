from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'comment']

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Комментарий к заказу'}),
        }

