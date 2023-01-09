from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from game.models import Player


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            player = Player.objects.create(user=user)
        return user
