from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Post


class PostListsView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-publish']
    queryset = Post.objects.all()
    # template_name = 'blogs/post_list.html'
    template_name = 'blogs/post_list_paginate.html' # Notice the change here
    paginate_by = 2 # Notice the change here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def post_list_view_func_with_pagination(request):
    all_posts = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blogs/post_list_paginate_view_func.html', {'posts': posts})

'''
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

from Blogs.models import Post
from .forms import AddNewPost, ReviewPostForm


# Create your views here.

def list_posts(request):
    if request.method == "GET":
        all_posts = Post.objects.filter(active=1).order_by('-id')
        return render(request, "Blogs/post_list.html", {'all_posts': all_posts})


def post_list_view_func_with_pagination(request):

    all_posts = Post.objects.all()
    page = request.GET.get('page', 2)

    paginator = Paginator(all_posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blogs/post_list_paginate_with_view_func.html', {'posts': posts})
    
    
class PostListsView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created']
    queryset = Post.objects.all()
    # template_name = 'blogs/post_list.html'
    template_name = 'blogs/post_list_paginate.html' # Notice the change here
    paginate_by = 4 # Notice the change here.


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'Blogs/post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slugss'


class AddNewPost(LoginRequiredMixin, View):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('blogs_list_posts')
    form_class = AddNewPost
    template_name = 'Blogs/post_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = f"{form.instance.author.first_name}-{form.instance.author.id}-{slugify(form.instance.title)}"
            # print("Before form save")
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form': form})
    
    
class ReviewPost(CreateView):
    context_object_name = 'review'
    form_class = ReviewPostForm
    template_name = 'Blogs/post_review_form.html'
    success_url = reverse_lazy('courses_index_page')
'''