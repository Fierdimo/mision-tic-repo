from django.urls import path
from .views import Listar, Detail

urlpatterns = [
    path('toys', Listar.as_view(), name='listar'),
    path('details', Detail.as_view(), name='details')
]