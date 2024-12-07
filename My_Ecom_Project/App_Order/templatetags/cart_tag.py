from django import template
from App_Order.models import Order

register = template.Library()

def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)
    
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0
    
register.filter("cart_totals", cart_total)