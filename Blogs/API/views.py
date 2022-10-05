from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from ..models import Post


def json_post_list(request):
    posts = Post.objects.all()
    all_posts = {"posts": list(posts.values())}
    return JsonResponse(all_posts)