from datetime import datetime
from django import template
register = template.Library()

@register.filter("timestamp")
def timestamp(value):
    
    format = "%Y-%m-%d %H:%M:%S.%f"
    
    try:
        return datetime.strptime(value, format)
    except AttributeError:
        return ''