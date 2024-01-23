from django import template
import re

register = template.Library()


@register.filter(name="has_tag")
def has_tag(messages, tag):
    return any(message.tags == tag for message in messages)


@register.filter(name="starts_with")
def starts_with(messages, tag):
    return messages.startswith(tag)


@register.filter(name="get")
def get(mapping, key):
    return mapping.get(key, "")


@register.filter(name="split")
def split(value, index):
    """
    Custom filter to return the nth element of a split using pipe '|'
    as separator.

    Usage: {{ your_string_variable|split:"index" }}
    """
    if value:
        elements = value.split("|")
        if 0 <= index < len(elements):
            return elements[index]
    return ""
