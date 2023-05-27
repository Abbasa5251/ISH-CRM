from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from transaction.models import Transaction
from transaction.serializers import TransactionsSerializer

@api_view(['GET'])
def all_transactions(request):
    if request.method == 'GET':
        trans = Transaction.objects.all()
        trans = TransactionsSerializer(trans, many=True)
        return Response(data=trans.data, status=status.HTTP_200_OK)
