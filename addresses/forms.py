from django import forms

from .models import Address


class UrlForm(forms.ModelForm):

    url = forms.CharField(
        label = "Url",
        max_length=256,
        required=True,
    )
    
    name = forms.CharField(
        label = "Name",
        max_length=128,
        required=False,
    )

    # def clean(self):
    #     cleaned_data = super(UrlForm, self).clean()
    #     return cleaned_data

    class Meta:
        model = Address
        fields = ('url', 'name', )