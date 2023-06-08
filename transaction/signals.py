from django.db.models.signals import post_save, pre_delete
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

@receiver(pre_delete, sender=Transaction)
def delete_transaction_update_payment_due(sender, instance, using, **kwargs):
    if instance.type == "DEBIT":
        instance.customer.payment_due += instance.amount
    elif instance.type == 'CREDIT':
        instance.customer.payment_due -= instance.amount
    instance.customer.save()
    