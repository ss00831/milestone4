from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    number_people = int(request.POST.get('number_people'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += number_people
    else:
        cart[item_id] = number_people

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)