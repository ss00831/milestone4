from django.conf import settings
from django.shortcuts import get_object_or_404
from tourprograms.models import Tourprogram


def cart_contents(request):

    cart_items = []
    total_adult = 0
    tourprogram_count = 0
    cart = request.session.get('cart', {})
    gift_event = settings.GIFT_THRESHOLD

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            tourprogram = get_object_or_404(Tourprogram, pk=item_id)
            total_adult += item_data * tourprogram.priceadult
            tourprogram_count += item_data
            cart_items.append({
                'item_id': item_id,
                'number_people_adult': item_data,
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

    if total_adult < settings.GIFT_THRESHOLD:
        gift_event = settings.GIFT_THRESHOLD - total_adult
    else:
        gift_event = 0

    grand_total = total_adult

    context = {
        'cart_items': cart_items,
        'total_adult': total_adult,
        'tourprogram_count': tourprogram_count,
        'gift_event': gift_event,
        'gift_threshold': settings.GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
