from django import forms

from cmsflex.models import FlexItem


class FlexForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk is not None:
            self.fields['create'].initial = 0

    create = forms.CharField(
        label="Create # flex items",
        help_text="Create this number of flex items",
        max_length=80,
    )

    class Meta:
        model = FlexItem
        exclude = ('page', 'position', 'placeholder',
                   'language', 'plugin_type')
