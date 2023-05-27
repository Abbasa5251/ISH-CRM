from rest_framework import serializers

from customer.models import Customer
from transaction.serializers import TransactionSerializer

class CustomerSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()
    transaction_count = serializers.SerializerMethodField()
    total_transaction_amount = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        exclude = (
            'created_at', 'modified_at'
        )

    def get_transactions(self, obj):
        data = []
        for t in obj.transactions.all():
            trans = TransactionSerializer(t)
            data.append(trans.data)
        return data

    def get_transaction_count(self, obj):
        return obj.transactions.all().count()

    def get_total_transaction_amount(self, obj):
        amount = 0
        for transaction in obj.transactions.all():
            amount += transaction.amount
        return amount
    