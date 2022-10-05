from django.urls import path
from .views import json_post_list

urlpatterns = [
    path('json_all_posts/', json_post_list, name='api_json_all_courses'),
]