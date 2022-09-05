from django import forms

from cmsflex.models import FlexItem


class FlexForm(forms.ModelForm):

    create = forms.CharField(
        label="Create # flex items",
        help_text="Create this number of flex items",
        max_length=80

    )

    class Meta:
        model = FlexItem
        exclude = ('page', 'position', 'placeholder',
                   'language', 'plugin_type')
