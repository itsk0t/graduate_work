from django import forms

from technical.models import UserAddress, City


class UserAddressForm(forms.ModelForm):
    street = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Улица'}))
    house = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Дом'}))
    entrance = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Подъезд'}))
    floor = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Этаж'}))
    apartment = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Квартира'}))
    city_id = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-select w-100'}))

    class Meta:
        model = UserAddress
        fields = ['city_id', 'street', 'house', 'entrance', 'floor', 'apartment']
