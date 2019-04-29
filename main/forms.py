from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True})
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
