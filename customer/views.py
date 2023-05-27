from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer.models import Customer
from customer.serializers import CustomerSerializer

@api_view(['GET'])
def all_customers(request):
    if request.method == "GET":
        customers = Customer.objects.filter(is_active=True)
        customers = CustomerSerializer(customers, many=True)
        return Response(customers.data, status=status.HTTP_200_OK)
