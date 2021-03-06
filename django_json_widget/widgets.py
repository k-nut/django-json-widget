from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.conf import settings


class JSONEditorWidget(forms.Widget):
    class Media:
        css = {'all': (settings.STATIC_URL + 'dist/jsoneditor.css',)}
        js = (settings.STATIC_URL + 'dist/jsoneditor.js', )

    template_name = 'django_json_widget.html'

    def render(self, name, value, attrs=None):
        context = {
            'data': value,
            'name': name
        }

        return mark_safe(render_to_string(self.template_name, context))
