from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from tourprograms.models import Tourprogram


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified tour program to the shopping cart """

    tourprogram = get_object_or_404(Tourprogram, pk=item_id)
    number_people_adult = int(request.POST.get('number_people_adult'))
    redirect_url = request.POST.get('redirect_url')
    date = None
    if 'select_departure_date' in request.POST:
        date = request.POST['select_departure_date']
    cart = request.session.get('cart', {})

    if date:
        if item_id in list(cart.keys()):
            if date in cart[item_id]['items_by_date'].keys():
                cart[item_id]['items_by_date'][date] += number_people_adult
                messages.success(request,
                                 (f'Updated date {date.upper()} '
                                  f'{tourprogram.name} people to '
                                  f'{cart[item_id]["items_by_date"][date]}'))
            else:
                cart[item_id]['items_by_date'][date] = number_people_adult
                messages.success(request,
                                 (f'Added date {date.upper()} '
                                  f'{tourprogram.name} to your cart'))
        else:
            cart[item_id] = {'items_by_date': {date: number_people_adult}}
            messages.success(request,
                             (f'Added date {date.upper()} '
                              f'{tourprogram.name} to your cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += number_people_adult
            messages.success(request,
                             (f'Updated {tourprogram.name} '
                              f'people to {cart[item_id]}'))
        else:
            cart[item_id] = number_people_adult
            messages.success(request, f'Added {tourprogram.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the number of people of the specified tour program
    to the specified amount
    """
    tourprogram = get_object_or_404(Tourprogram, pk=item_id)
    number_people_adult = int(request.POST.get('number_people_adult'))
    maximum = tourprogram.maximum
    date = None
    if 'select_departure_date' in request.POST:
        date = request.POST['select_departure_date']
    cart = request.session.get('cart', {})

    if date:
        if number_people_adult > 0 and number_people_adult <= maximum:
            cart[item_id]['items_by_date'][date] = number_people_adult
            messages.success(request,
                             (f'Updated date {date.upper()} '
                              f'{tourprogram.name} people to '
                              f'{cart[item_id]["items_by_date"][date]}'))
        elif number_people_adult == 0:
            messages.error(request,
                           ('0/null value and texts are not acceptable. '
                            'If you want to remove this item, '
                            'please click the trash can icon.'))
        elif number_people_adult > tourprogram.maximum:
            messages.error(request,
                           (f'The maximum of this tour is '
                            f'{tourprogram.maximum}.'))
            if not cart[item_id]['items_by_date']:
                messages.error(request,
                               (f'The maximum of this tour is '
                                f'{tourprogram.maximum}.'))
        else:
            messages.error(request, 'Wrong 2.')
    else:
        if number_people_adult > 0 and number_people_adult <= maximum:
            cart[item_id] = number_people_adult
            messages.success(request,
                             (f'Updated {tourprogram.name} '
                              f'people to {cart[item_id]}'))
        elif number_people_adult == 0:
            messages.error(request,
                           ('0/null value and texts are not acceptable. '
                            'If you want to remove this item,'
                            'please click the trash can icon.'))
        else:
            messages.error(request,
                           (f'The maximum of this tour is '
                            f'{tourprogram.maximum}.'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        tourprogram = get_object_or_404(Tourprogram, pk=item_id)
        date = None
        if 'select_departure_date' in request.POST:
            date = request.POST['select_departure_date']
        cart = request.session.get('cart', {})

        if date:
            del cart[item_id]['items_by_date'][date]
            if not cart[item_id]['items_by_date']:
                cart.pop(item_id)
            messages.success(request,
                             (f'Removed date {date.upper()} '
                              f'{tourprogram.name} from your cart'))
        else:
            cart.pop(item_id)
            messages.success(request,
                             (f'Removed {tourprogram.name} from your cart'))

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
