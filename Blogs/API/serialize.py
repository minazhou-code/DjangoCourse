from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date
from rest_framework import serializers
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256, blank=False)
    slug = serializers.SlugField(max_length=256, unique_for_date='created')
    excerpt = serializers.CharField(max_length=512, blank=False)
    content = serializers.CharField(max_length=4096, blank=False)
    active = serializers.BooleanField(default=True)
    created = serializers.DateField(default=timezone.now)
    author = serializers.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')