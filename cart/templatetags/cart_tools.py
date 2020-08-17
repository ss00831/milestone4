from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(priceadult, number_people_adult):
    return priceadult * number_people_adult