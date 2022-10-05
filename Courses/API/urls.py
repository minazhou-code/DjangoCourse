from django.urls import path
from .views import json_course_list, json_get_specific_course, api_course_list, api_course_detail

urlpatterns = [
    path('json_all_courses/', json_course_list, name='api_json_all_courses'),
    path('json_get_specific_course/<int:course_id>/', json_get_specific_course, name='api_json_get_specific_course'),
    path('courses/vfs_list/', api_course_list, name='courses_vfs_list'), # New Entry
    path('courses/vfs_detail/<int:pk>', api_course_detail, name='courses_vfs_detail'), # New Entry
]