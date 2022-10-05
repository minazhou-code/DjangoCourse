# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    class Meta:
        db_table = 'post'

    title = models.CharField(max_length=256, blank=False)
    slug = models.SlugField(max_length=256, unique_for_date='created')
    excerpt = models.CharField(max_length=512, blank=False)
    content = models.CharField(max_length=4096, blank=False)
    active = models.BooleanField(default=True)
    created = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')

    def __str__(self):
        post = f"{self.title} by {self.author.get_full_name()}"
        return post

    def clean(self):
        print("Model Clean")
        super().clean()
        # self.slug = f"{self.author.first_name}-{self.author.id}-{slugify(self.title)}"
        self.validate_unique()

class PostReview(models.Model):
    class Meta:
        db_table = 'post_review'

    RATINGS = [('5', "Excellent"),
               ('4', "Very Good"),
               ('3', "Good"),
               ('2', "Poor"),
               ('1', "Very Poor")]

    rating = models.CharField(max_length=1, choices=RATINGS, default='4')
    comment = models.CharField(max_length=1024, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_reviews")

    def __str__(self):
        post_review = f"{self.post.title} with {self.rating} rating"
        return post_review