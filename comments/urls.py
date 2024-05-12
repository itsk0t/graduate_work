from django.urls import path

from comments.views import reviews_view

app_name = 'comments'

urlpatterns = [
    path('', reviews_view, name='reviews_list')
]