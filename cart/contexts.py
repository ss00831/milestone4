from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    tourprogram_count = 0

    gift_event_1 = settings.GIFT_THRESHOLD_1
    gift_event_2 = settings.GIFT_THRESHOLD_2

    
    grand_total = total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'tourprogram_count': tourprogram_count,
        'gift_event_1': gift_event_1,
        'gift_event_2': gift_event_2,
        'gift_threshold_1': settings.GIFT_THRESHOLD_1,
        'gift_threshold_2': settings.GIFT_THRESHOLD_2,
        'grand_total': grand_total,
    }

    return context