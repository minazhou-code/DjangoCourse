
from django.contrib.auth.models import User
from django.db import models
# import sys
# sys.path.append('../Courses')
#
# from ..models import Course

# Create your models here.
# from Courses.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver

class CourseEnroll(models.Model):
    class Meta:
        db_table = 'course_enroll'
        verbose_name_plural = "Course Enroll"

    COURSE_STATUS = [('C', 'Compete'),
                     ('E', 'Enrolled'),
                     ('I', 'InProgress'),
                     ]
    status = models.CharField(max_length=1, choices=COURSE_STATUS, default='E')
    student = models.ForeignKey(User, on_delete=models.PROTECT, related_name='students')
    course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE, related_name='enrolments')

    objects = models.Manager()

    def __str__(self):
        course_enrollment = f"{self.student.get_full_name()}, enrolled for {self.course.name}"
        return course_enrollment


class UserProfile(models.Model):
    class Meta:
        db_table = 'user_profile'
        verbose_name = 'user_profile'
        verbose_name_plural = 'User Profile'
    is_student = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile/%Y/%m/%d', verbose_name='Profile Image',
                                      name="profile_image", null=True)


# Add this function after the class definition
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()

# user visits
class PageView(models.Model):
    page = models.CharField(max_length=50, blank=False)
    hits = models.IntegerField(default=0)