# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.contrib.auth import logout
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

