from django import template


register = template.Library()


@register.filter(name='calculate_percentage_saved')
def calculate_percentage_saved():
    return 
