from django import forms

from .models import Check


class CheckForm(forms.ModelForm):

    # type = forms.ChoiceField(
    #     label = "Url",
    #     max_length=256,
    #     required=True,
    # )
    
    # name = forms.CharField(
    #     label = "Name",
    #     max_length=128,
    #     required=False,
    # )

    # def clean(self):
    #     cleaned_data = super(UrlForm, self).clean()
    #     return cleaned_data

    class Meta:
        model = Check
        fields = ('check_type', 'succes_value', 'description')