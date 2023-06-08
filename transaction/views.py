from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer, CreateTransactionSerializer

@api_view(['GET', 'POST'])
def all_transactions(request):
    if request.method == 'GET':
        trans = Transaction.objects.all()
        trans = TransactionSerializer(trans, many=True)
        return Response(data=trans.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = CreateTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_transaction(request, pk):
    if request.method == "DELETE":
        try:
            transactions = Transaction.objects.filter(pk=pk)
            if len(transactions) == 0:
                data = {"message": f"The transaction with id {pk} doen't exist"}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            transaction = transactions.first()
            transaction.delete()
            data = {"message": f"The transaction with id {pk} has been successfully deleted!"}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": f"There was an error while deleting the data", "errors": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
