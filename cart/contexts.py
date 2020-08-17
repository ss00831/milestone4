from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tourprograms.models import Tourprogram


def cart_contents(request):

    cart_items = []
    total_adult = 0
    #total_child = 0
    tourprogram_count = 0
    cart = request.session.get('cart', {})
    #number_people_adult = request.form.get('number_people_adult')
    #number_people_child = request.form.get('number_people_child')
    # ttl_people = number_people_adult + number_people_child

    gift_event_1 = settings.GIFT_THRESHOLD_1
    gift_event_2 = settings.GIFT_THRESHOLD_2

    for item_id, number_people_adult in cart.items():
        tourprogram = get_object_or_404(Tourprogram, pk=item_id)
        total_adult += number_people_adult * tourprogram.priceadult
        #total_child += number_people_child * tourprogram.pricechild
        
        tourprogram_count += number_people_adult
        cart_items.append({
            'item_id': item_id,
            'number_people_adult': number_people_adult,
            #'number_people_child': number_people_child,
            'tourprogram': tourprogram,
        })
    
    grand_total = total_adult
    # + total_child
    
    context = {
        'cart_items': cart_items,
        'total_adult': total_adult,
        # 'total_child': total_child,
        'tourprogram_count': tourprogram_count,
        'gift_event_1': gift_event_1,
        'gift_event_2': gift_event_2,
        'gift_threshold_1': settings.GIFT_THRESHOLD_1,
        'gift_threshold_2': settings.GIFT_THRESHOLD_2,
        'grand_total': grand_total,
    }

    return context