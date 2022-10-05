from django.utils.datetime_safe import date
from rest_framework import serializers

from datetime import date

from ..models import Course


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    short_desc = serializers.CharField(max_length=1024)
    description = serializers.CharField(max_length=4096)
    duration = serializers.IntegerField()
    delivery_mode = serializers.CharField(max_length=3)
    keywords = serializers.CharField(max_length=512)
    date_added = serializers.DateField(write_only=True, default=date.today())
    active = serializers.CharField(max_length=1)
    date_active = serializers.DateField(write_only=True, default=None)
    max_students = serializers.IntegerField()
    instructor_id = serializers.IntegerField()

    def create(self, validated_data):
        return Course.my_courses.create(**validated_data)