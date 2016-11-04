from django.forms.widgets import Widget
from django.forms.widgets import Input


class Display(Widget):
    def render(self, name, value=None, attrs=None):
        widget = '<span>{}</span>'.format(value)
        attrs['style'] = 'display:none'
        attrs['type'] = 'text'
        widget += Input().render(name, value, attrs)
        return widget
