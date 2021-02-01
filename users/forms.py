from django import forms

from .models import UserProfile


class RegisterForm(forms.Form):

    username = forms.CharField(
        label = "Username",
        max_length=64,
        required=True,
    )
    
    email = forms.EmailField(
        label = "Email",
        max_length=256,
        required=True,
    )
    
    raw_password = forms.CharField(
        label = "Password",
        max_length=256,
        required=True,
        help_text = "10 caractères minimum",
        widget=forms.PasswordInput(),
    )
    
    raw_password_confirmation = forms.CharField(
        label = "Password",
        max_length=256,
        required=True,
        widget=forms.PasswordInput(),
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        raw_password = cleaned_data.get('raw_password')
        raw_password_confirmation = cleaned_data.get('raw_password_confirmation')
        
        if len(raw_password) < 10:
            raise forms.ValidationError("The password must be at least 10 character long")
        
        if raw_password and raw_password_confirmation:
            if raw_password != raw_password_confirmation:
                raise forms.ValidationError("You must type the same password in both fields")
        
        try:
            UserProfile.objects.get(username=cleaned_data['username'])
        except UserProfile.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("This User already exists")

        try:
            UserProfile.objects.get(email=cleaned_data['email'])
        except UserProfile.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("This email is already in use")

        return cleaned_data