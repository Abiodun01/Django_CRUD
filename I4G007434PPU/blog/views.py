from dataclasses import fields
from pyexpat import model
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# Create your views here.
class PostListView(CreateView):
    #specify model to be used
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):

    model = Post

class PostUpdateView(UpdateView):

    model = Post
    fields = "__alll__"
    success_url = reverse_lazy("blog:all")
    
class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")