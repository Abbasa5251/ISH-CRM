from typing import Any
import uuid
from django.db import models

from customer.models import Customer

TRANSACTION_TYPE = (
    ("DEBIT", "Debit"), # Customer has paid us
    ("CREDIT", "Credit") # Customer has taken the stock from us
)

class Transaction(models.Model):
    id = models.UUIDField(verbose_name="ID", default=uuid.uuid4, primary_key=True, unique=True)
    customer = models.ForeignKey(to=Customer, related_name="transactions", on_delete=models.CASCADE)
    amount = models.IntegerField()
    paid_on = models.DateTimeField()
    type = models.CharField(verbose_name="Type", max_length=10, choices=TRANSACTION_TYPE, default="DEBIT")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.customer.name} - {self.amount}"
