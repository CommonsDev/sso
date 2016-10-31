from django.forms.widgets import Widget


class Display(Widget):
    def render(self, name, value=None, attrs=None):
        return '<span>{}</span>'.format(value)
