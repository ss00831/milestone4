from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from tourprograms.models import Tourprogram

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart  """

    tourprogram = get_object_or_404(Tourprogram, pk=item_id)
    number_people_adult = int(request.POST.get('number_people_adult'))
    #number_people_child = int(request.POST.get('number_people_child'))
    #ttl_people = number_people_adult + number_people_child
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += number_people_adult
        messages.success(request, f'Updated {tourprogram.name} people to {cart[item_id]}')
    else:
        cart[item_id] = number_people_adult
        messages.success(request, f'Added {tourprogram.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the number of people of the specified tour program to the specified amount"""

    tourprogram = get_object_or_404(Tourprogram, pk=item_id)
    number_people_adult = int(request.POST.get('number_people_adult'))
    
    cart = request.session.get('cart', {})

    if number_people_adult > 0:
        cart[item_id] = number_people_adult
        messages.success(request, f'Updated {tourprogram.name} number of adults {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {tourprogram.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        tourprogram = get_object_or_404(Tourprogram, pk=item_id)
        size = None
        if 'tourprogram_size' in request.POST:
            size = request.POST['tourprogram_size']
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {tourprogram.name} from your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500) 