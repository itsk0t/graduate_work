from django.shortcuts import render
from technical.models import Point, City, ContactInf, AboutInf


def contacts_view(request):
    city = City.objects.all()
    point = Point.objects.filter(stop=True)
    contact_inf = ContactInf.objects.all()

    return render(request, 'technical/contacts.html', {'city': city, 'point': point, 'contact_inf': contact_inf})


def about_us_view(request):
    inf = AboutInf.objects.all()

    return render(request, 'technical/about_us.html', {'inf': inf})
