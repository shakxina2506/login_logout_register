from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    pk_url_kwarg = 'pk'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_create.html'

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_update.html'
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_list')
