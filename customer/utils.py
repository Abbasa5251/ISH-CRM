from customer.models import Customer

def total_transaction_amount_for_customer(customer_obj: Customer, transaction_type: str | None=None):
    if not customer_obj:
         return 0
    
    amount = 0
    if transaction_type:
        filtered_query = customer_obj.transactions.filter(type=transaction_type)
    else:
        filtered_query = customer_obj.transactions.all()

    for transaction in filtered_query:
        amount += transaction.amount
    return amount
