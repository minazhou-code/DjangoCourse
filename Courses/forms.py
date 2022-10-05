from django import forms

from .models import Course


class NewCourseUsingForm(forms.Form):
    DELIVERY_MODE = [('ON', 'Online'),
                    ('OFF', 'Offline'),
                    ('REC', 'Recorded Session'),
                    ]
    course_name = forms.CharField(label='Course name: ', max_length=256)
    short_desc = forms.CharField(label='Short Description: ', max_length=1024)
    desc = forms.CharField(label='Description: ', max_length=1024)
    instructor = forms.CharField(label='Instructor: ', max_length=1024)
    duration = forms.DecimalField(label="Duration:", min_value=1, max_value=120)
    delivery_mode = forms.ChoiceField(choices=DELIVERY_MODE)
    keywords = forms.CharField(label='Keywords: ', max_length=1024)

    def clean_course_name(self):
        print("In - clean_course_name")
        if Course.my_courses.filter(name=self.cleaned_data["course_name"]).exists():
            raise forms.ValidationError(f'Course Name {self.cleaned_data["course_name"]}exists. Use a unique name', code='Duplicate Course name')
        return self.cleaned_data["course_name"]

    def clean(self):
        super.clean()
        print("In - Clean() - to show the sequence of execution.")

class NewCourseFormUsingModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {'name': "Course Name"}
        help_texts = {'name': 'Provide a unique name of the Course'}
        widgets = {'description': forms.Textarea(attrs={'cols': 100, 'rows': 4})}