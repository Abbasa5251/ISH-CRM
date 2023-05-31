from rest_framework import serializers

from customer.models import Customer
from transaction.serializers import TransactionSerializer
from customer.utils import total_transaction_amount_for_customer


class CustomersSerializers(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    transaction_count = serializers.SerializerMethodField()
    total_transaction_amount = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = "__all__"
    
    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_transaction_count(self, obj):
        return obj.transactions.all().count()

    def get_total_transaction_amount(self, obj):
        return total_transaction_amount_for_customer(obj)

class CustomerSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()
    transaction_count = serializers.SerializerMethodField()
    total_transaction_amount = serializers.SerializerMethodField()
    total_transaction_debit_amount = serializers.SerializerMethodField()
    total_transaction_credit_amount = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        exclude = (
            'created_at', 'modified_at'
        )

    def get_transactions(self, obj):
        return [TransactionSerializer(t).data for t in obj.transactions.all()]

    def get_transaction_count(self, obj):
        return obj.transactions.all().count()

    def get_total_transaction_amount(self, obj):
        return total_transaction_amount_for_customer(obj)

    def get_total_transaction_debit_amount(self, obj):
        return total_transaction_amount_for_customer(obj, "DEBIT")

    def get_total_transaction_credit_amount(self, obj):
        return total_transaction_amount_for_customer(obj, "CREDIT")
