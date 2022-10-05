from django import forms
from .models import Post
from .models import PostReview


class AddNewPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created', 'author']
        labels = {'title': "Post Title", 'excerpt': 'Short Summary', 'content': "Post Content"}
        widgets = {'content': forms.Textarea(),
                   'slug': forms.HiddenInput(attrs={'value': 'aa'}),
                   }


class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = PostReview
        fields = "__all__"