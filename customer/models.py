import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(verbose_name="ID", default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(verbose_name="Name", max_length=128)
    email = models.CharField(verbose_name="Email", max_length=128, null=True, blank=True)
    phone = models.CharField(verbose_name="Phone Number", max_length=12, null=True, blank=True)
    address = models.TextField(verbose_name="Address")
    payment_due = models.IntegerField(verbose_name="Payment Due")
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    # payday = models.CharField(verbose_name="Pay Day") #0010001 (starting from Monday)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])
