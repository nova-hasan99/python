from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Django ফর্ম ফিল্ডে CSS ক্লাস যোগ করে।"""
    return field.as_widget(attrs={"class": css_class})
