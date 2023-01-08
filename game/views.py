from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import TemplateView, FormView
from game.forms import CreateUserForm
from django.template import RequestContext
from django.http import HttpResponseNotFound


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


def handler404(request, exception, template_name='404.html'):
    data = {
        'name': '127.0.0.1'
    }
    response = render(request, template_name, data)
    response.status_code = 404
    return response

class MainView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        ...
