from django import template
import re

register = template.Library()


@register.filter(name="placeholder")
def placeholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value


