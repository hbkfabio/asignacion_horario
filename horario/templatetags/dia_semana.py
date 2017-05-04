from django.template.defaulttags import register
...
@register.filter(is_safe=True)
def get_item(dictionary, key):
    return dictionary.get(key)
