from django.db.models.signals import post_save
from django.dispatch import receiver

from transaction.models import Transaction

@receiver(post_save, sender=Transaction)
def update_payment_due(sender, instance, created, **kwargs):
    if created:
        if instance.type == "DEBIT":
            instance.customer.payment_due -= instance.amount
        elif instance.type == 'CREDIT':
            instance.customer.payment_due += instance.amount

        instance.customer.save()
