from django import forms


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
    tourprogram = forms.CharField(required=False)
    ordernumber = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
