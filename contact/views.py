from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm


# Sending email : https://docs.djangoproject.com/en/3.1/topics/email/
def contact(request):
    """ Display the user's profile. """
    contact_form = ContactForm(request.POST or None)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            contact_type = contact_form.cleaned_data['contact_type']
            tour_program_name = contact_form.cleaned_data['tour_program_name']
            order_number = contact_form.cleaned_data['order_number']
            phone = contact_form.cleaned_data['phone']
            message = contact_form.cleaned_data['message']
            send_mail(
                f"From {name}, <{email}>",
                f"Contact type: {contact_type}'\n'"
                f"Tour program: {tour_program_name}"
                f"'\n'Order number: {order_number}'\n'Phone:"
                f"{phone}'\n'message: {message}",
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
