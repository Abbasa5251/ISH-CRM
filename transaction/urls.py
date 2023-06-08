from django.urls import path

from transaction import views

urlpatterns = [
    path('', views.all_transactions, name='transactions'),
    path('<str:pk>', views.delete_transaction, name='delete_transaction'),
]
