# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_list_or_404,redirect
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Comment
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
