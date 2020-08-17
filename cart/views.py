from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart  """

    number_people_adult = int(request.POST.get('number_people_adult'))
    #number_people_child = int(request.POST.get('number_people_child'))
    #ttl_people = number_people_adult + number_people_child
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += number_people_adult
    else:
        cart[item_id] = number_people_adult

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the number of people of the specified tour program to the specified amount"""

    number_people_adult = int(request.POST.get('number_people_adult'))
    
    cart = request.session.get('cart', {})

    if number_people_adult > 0:
        cart[item_id] = number_people_adult
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        size = None
        if 'tourprogram_size' in request.POST:
            size = request.POST['tourprogram_size']
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500) 