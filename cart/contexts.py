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

    gift_event = settings.GIFT_THRESHOLD

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            tourprogram = get_object_or_404(Tourprogram, pk=item_id)
            total_adult += item_data * tourprogram.priceadult
            tourprogram_count += item_data
            cart_items.append({
                'item_id': item_id,
                'number_people_adult': item_data,
                # 'number_people_child': number_people_child,
                'tourprogram': tourprogram,
            })
        else: 
            tourprogram = get_object_or_404(Tourprogram, pk=item_id)
            for date, number_people_adult in item_data['items_by_date'].items():
                total_adult += number_people_adult * tourprogram.priceadult
                tourprogram_count += number_people_adult
                cart_items.append({
                    'item_id': item_id,
                    'number_people_adult': number_people_adult,
                    'tourprogram': tourprogram,
                    'date': date,
                })
    
    grand_total = total_adult  # + total_child
    
    context = {
        'cart_items': cart_items,
        'total_adult': total_adult,
        #'total_child': total_child,
        'tourprogram_count': tourprogram_count,
        'gift_event': gift_event,
        'gift_threshold': settings.GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context