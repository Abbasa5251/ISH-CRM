from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer.models import Customer
from customer.serializers import CustomerSerializer, CustomersSerializers

@api_view(['GET'])
def all_customers(request):
    if request.method == "GET":
        customers = Customer.objects.filter(is_active=True)
        customers = CustomersSerializers(customers, many=True)
        return Response(customers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def customer_detail(request, id):
    if request.method == "GET":
        customer = Customer.objects.get(id=id)
        customer = CustomerSerializer(customer)
        return Response(customer.data, status=status.HTTP_200_OK)
