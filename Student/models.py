# from django.contrib.auth.models import User
# from django.db import models
#
#
# # Create your models here.
# class CourseEnroll(models.Model):
#     class Meta:
#         db_table = 'course_enroll'
#         verbose_name_plural = "Course Enroll"
#
#     COURSE_STATUS = [('C', 'Compete'),
#                      ('E', 'Enrolled'),
#                      ('I', 'InProgress'),
#                      ]
#     status = models.CharField(max_length=1, choices=COURSE_STATUS, default='E')
#     student = models.ForeignKey(User, on_delete=models.PROTECT, related_name='students')
#     course = models.ForeignKey('Courses.Course', on_delete=models.CASCADE, related_name='enrolments')
#
#     objects = models.Manager()
#
#     def __str__(self):
#         course_enrollment = f"{self.student.get_full_name()}, enrolled for {self.course.name}"
#         return course_enrollment
