# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Resturant(models.Model):
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=120)
  image = models.ImageField(upload_to='resturants/')
  categories = models.CharField(max_length=120)
  location = models.CharField(max_length=120)
  price = models.IntegerField()
  vat = models.PositiveIntegerField(default=0)
  taste = models.PositiveIntegerField(choices=choices)
  person = models.PositiveIntegerField(choices=choices)
  details = models.TextField()
  slug = models.SlugField(unique=True, blank=True)
  likes = models.ManyToManyField(User,related_name='post_likes',blank=True)
  views = models.IntegerField(default=0, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  is_active = models.BooleanField(default=True)
  
