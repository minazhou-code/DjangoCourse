from django.contrib import admin
from .models import Course, course_rating

# Register your models here.
admin.site.register(Course)
admin.site.register(course_rating)


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('courses',)
    # Notice the change
    fieldsets = [
        ('Course Info', {'fields': ['name', 'instructor', 'duration']}),
        ('Details', {'fields': ['short_desc', 'description', 'keywords']}),
        ('More Info', {'fields': ['active', 'delivery_mode', 'max_students']}),
    ]