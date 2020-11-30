from django import template

register = template.Library()

@register.filter(name="klos")
def nx(value,arg):

    return value.replace(arg,'')

# register.filter('klo',klo)
