from django.urls import path
from customer import views

urlpatterns = [
    path('', views.all_customers, name="customers"),
    path('<uuid:id>', views.customer_detail, name="customer-detail"),
]
