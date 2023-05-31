from rest_framework import serializers

from transaction.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        exclude = (
            'created_at', 'modified_at', 'customer'
        )

    def get_customer_name(self, obj):
        return obj.customer.name

class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'amount', 'customer', 'paid_on', 'type', 'mode'
        )
