from django import forms

from technical.models import UserAddress


class UserAddressForm(forms.ModelForm):
    street = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Улица'}))
    house = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Дом'}))
    entrance = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Подъезд'}))
    floor = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Этаж'}))
    apartment = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Квартира'}))

    class Meta:
        model = UserAddress
        fields = ['city_id', 'street', 'house', 'entrance', 'floor', 'apartment']
