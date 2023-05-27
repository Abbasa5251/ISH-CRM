from django.urls import path

from transaction import views

urlpatterns = [
    path('', views.all_transactions, name='transactions'),
]
