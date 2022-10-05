from django.db import models

# Create your models here.
class Course(models.Model):
    DELIVERY_MODE = [('ON', 'Online'),
                     ('OFF', 'Offline'),
                     ('REC', 'Recorded Session'),
                     ]
    # id = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=256, blank=False)
    short_desc = models.CharField(max_length=1024, blank=False)
    description = models.TextField(blank=False)
    instructor = models.CharField(max_length=150, blank=False)
    duration = models.IntegerField(blank=False)
    delivery_mode = models.CharField(max_length=3, choices=DELIVERY_MODE, default='ON')
    keywords = models.CharField(max_length=1024, blank=False)
    date_added = models.DateField(verbose_name='date added', auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    my_courses = models.Manager()
    def __str__(self):
        return f"{self.name} course by {self.instructor}"


# class course_rating(models.Model):
#     name = models.CharField(max_length= 256, blank=False)
#     rating = models.IntegerField(blank=False) # No need to use max_length for IntegerField
#     def __str__(self):
#         return f"The rating of {self.name} is {self.rating}"

class course_rating(models.Model):
    ratings = [
        (5, "Excellent"),
        (4, "Good"),
        (3, "Not bad"),
        (2, "Not well"),
        (1, "Poor")
    ]

    # rating = models.PositiveSmallIntegerField(blank=False,default=1,validators=(MinValueValidator(1), MaxValueValidator(5)))
    rating = models.IntegerField(blank=False, default=1, choices=ratings)
    # course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"Rating of {self.course.name} is {self.rating}"