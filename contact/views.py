from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):
    """ Display the user's profile. """
    contact_form = ContactForm(request.POST or None)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            contact_type = contact_form.cleaned_data['contact_type']
            tourprogram = contact_form.cleaned_data['tourprogram']
            ordernumber = contact_form.cleaned_data['ordernumber']
            phone = contact_form.cleaned_data['phone']
            message = contact_form.cleaned_data['message']
            send_mail(
                f"From {name}, <{email}>", 
                f"Contact type: {contact_type}'\n'Tour program: {tourprogram}'\n'Order number: {ordernumber}'\n'Phone: {phone}'\n'message: {message}", 
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False
            )
            print(send_mail)
            return redirect('contact_success')

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def contact_success(request):
    return render(request, 'contact/contact_success.html')