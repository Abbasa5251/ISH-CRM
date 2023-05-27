from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from transaction.models import Transaction
from transaction.serializers import TransactionsSerializer, CreateTransactionSerializer

@api_view(['GET', 'POST'])
def all_transactions(request):
    if request.method == 'GET':
        trans = Transaction.objects.all()
        trans = TransactionsSerializer(trans, many=True)
        return Response(data=trans.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = CreateTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_201_CREATED)
