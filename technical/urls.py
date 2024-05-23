from django.urls import path
from technical.views import contacts_view, about_us_view

app_name = 'technical'

urlpatterns = [
    path('contacts/', contacts_view, name='contacts'),
    path('about_us/', about_us_view, name='about_us'),
]
