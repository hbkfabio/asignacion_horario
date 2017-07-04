from django.template.defaulttags import register
from django.template.defaultfilters import linebreaksbr, urlize
...
@register.filter(is_safe=True, needs_autoescape=True)
def get_item(dictionary, key, autoescape=True):
    return dictionary.get(key)
