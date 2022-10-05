from django.shortcuts import render
from django.http import JsonResponse

from django.db import models
from ..models import Course
from rest_framework.response import Response
from .serialize import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def json_course_list(request):
    courses = Course.my_courses.all()
    all_courses = {"courses": list(courses.values())}
    return JsonResponse(all_courses)

def json_get_specific_course(request, course_id):
    course_found = Course.my_courses.filter(pk=course_id).count()
    print(course_found)
    if not course_found:
        return JsonResponse(status=404, data={'status': 'false', 'message': f'Course with ID {course_id} not found'})
    else:
        course = Course.my_courses.get(pk=course_id)
        course_data = {"id"                  : course.id,
                       "course_name"         : course.name,
                       "course_details"      : course.description,
                       "course_instructor"   : course.instructor,
                       "course_duration"     : course.duration,
                       "course_delivery_mode": course.delivery_mode,
                       "course_keywords"     : course.keywords,
                       "course_added_on"     : course.date_added,
                       "course_active_status": course.active,
                       "course_active_on"    : course.date_active}
        return JsonResponse(course_data)



@api_view(['GET', 'POST'])
def api_course_list(request):
    if request.method == 'GET':
        courses = Course.my_courses.all()
        serialized_courses = CourseSerializer(courses, many=True)
        return Response(serialized_courses.data)
    elif request.method == "POST":
        serialized_course = CourseSerializer(data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        else:
            return Response(serialized_course.errors)


@api_view()
def api_course_detail(request, pk):
    course_found = Course.my_courses.filter(pk=pk).count()
    if not course_found:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        course = Course.my_courses.get(pk=pk)
        serialized_course = CourseSerializer(course)
        return Response(serialized_course.data)