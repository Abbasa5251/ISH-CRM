from rest_framework import serializers

from transaction.models import Transaction

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = (
            'created_at', 'modified_at'
        )
        depth = 1

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id', 'amount', 'paid_on', 'mode'
        )

class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'amount', 'customer', 'paid_on', 'type', 'mode'
        )
