from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import TemplateView, FormView
from game.forms import CreateUserForm


class RegisterUser(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    # def get_success_url(self):
    #     return reverse_lazy('home')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class MainView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        ...
