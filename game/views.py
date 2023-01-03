from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from game.forms import CreateUserForm


class MainView(TemplateView):
    template_name = 'main.html'

    def get(self, request):
        ...


class RegisterFormView(FormView):
    form_class = CreateUserForm
    success_url = ''
    template_name = 'register.html'


class LoginView(TemplateView):
    ...
