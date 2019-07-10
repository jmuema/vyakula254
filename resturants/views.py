# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RestaurantCreateForm
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.

class RestaurantListView(ListView):
    queryset = Restaurant.objects.all()
    paginate_by = 6
    template_name = 'restaurants/restaurant_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        author = self.request.GET.get('author')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(details__icontains=q)
            ).distinct()
        if cat:
            queryset = queryset.filter(categories__icontains=cat)

        if author:
            queryset = queryset.filter(user__username=author)
        return queryset

    # @method_decorator(login_required)
    # def post(self, request, *args, **kwargs):
    #     post_id = request.POST.get('unlike')
    #     post_id2 = request.POST.get('like')
    #     if post_id is not None:
    #         post = get_object_or_404(Restaurant, id=post_id)
    #         post.likes.remove(request.user)
    #     if post_id2 is not None:
    #         post_id2 = request.POST.get('like')
    #         post = get_object_or_404(Restaurant, id=post_id2)
    #         post.likes.add(request.user)
    #     return redirect('home')

