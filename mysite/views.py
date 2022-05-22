from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthUserForm, RegisterUserForm
from .models import Item


def index(request):
    item_list = Item.objects.all()
    return render(request, 'mysite/index.html', {'list': item_list})


def detail(request, id):
    item = Item.objects.get(pk=id)
    return render(request, "mysite/item.html", {"item": item})


class MyprojectLoginView(LoginView):
    template_name = 'mysite/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'mysite/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('index')