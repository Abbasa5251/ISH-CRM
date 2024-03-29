from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/customers/', include('customer.urls')),
    path('api/v1/transactions/', include('transaction.urls')),
]
