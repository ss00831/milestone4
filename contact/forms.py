from django import forms


"""
ChoiceField – Django Forms :
    https://www.geeksforgeeks.org/choicefield-django-forms/
"""
CONTACT_TYPE = (
    ("1", "General question"),
    ("2", "Group tour"),
    ("3", "Tour option / personal selection"),
    ("4", "(For include meal program) Notice for Allergi"),
    ("5", "Cancel / Change"),
    ("6", "Other"),
)


class ContactForm(forms.Form):
    contact_type = forms.ChoiceField(choices=CONTACT_TYPE)
    name = forms.CharField()
    tour_program_name = forms.CharField(required=False)
    order_number = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
