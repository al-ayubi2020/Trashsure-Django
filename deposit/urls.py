from django.urls import path
from .views import index

app_name = 'deposit'

urlpatterns = [
    path('', index, name='index'),
]