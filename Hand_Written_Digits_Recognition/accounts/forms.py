from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput( attrs={
                "class": "form-control"
    }))
    email = forms.EmailField(max_length=255, widget=forms.TextInput( attrs={
                "class": "form-control"
    })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
    }))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
    }))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)

        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError("This email is already in use")

        return email
        



class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput( attrs={
                "placeholder": "Enter Username",
                "class": "form-control"
    }))
    password = forms.CharField(label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "class": "form-control mt-4",
                "id": "user-password"
    }))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError("This is an invalid user")

        return username