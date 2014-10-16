from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary[key]

@register.filter
def field_type(field):
    return field.field.__class__.__name__

@register.filter(is_safe=True)
def css_class(field,css_class):
    if field_type(field) == 'BooleanField':
        return field
    else:
        return field.as_widget(attrs={'class': css_class})