from django.urls import path
from customer import views

urlpatterns = [
    path('', views.all_customers),
]
