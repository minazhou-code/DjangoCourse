from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewCourseUsingForm, NewCourseFormUsingModelForm
from .models import Course
from datetime import date
from django.db import connection
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# Create your views here.
def new_course(request):
    if request.method == "GET":
        print("Course - Get")
        return render(request, "Courses/new_course.html")
    elif request.method == "POST":
        form = request.POST
        insert_statement = """INSERT INTO courses_course(name, short_desc,description, instructor, duration, delivery_mode, keywords, date_added, date_updated) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = [form["course_name"], form["short_desc"], form["desc"], form["instructor"], form["duration"],
                  form["Delivery Mode"], form["keywords"], date.today().isoformat(), date.today().isoformat()]
        cursor = connection.cursor()
        cursor.execute(insert_statement, values)
        connection.commit()
        return render(request, "Courses/new_course.html")


def sample_form_view(request):
    if request.method == 'GET':
        return render(request, "Courses/sample_form.html", {'method': request.method})
    elif request.method == 'POST':
        input_data = ""
        for key, value in request.POST.items():
            input_data += f"{key} - {value}"
            input_data += '\n'
        print(input_data)
        context = {'method': request.method,
                   'input_data': input_data}
        return render(request, "Courses/sample_form.html", context=context)


def new_course_using_form(request):
    form = None
    if request.method == "GET":
        form = NewCourseUsingForm()
    elif request.method == "POST":
        form = NewCourseUsingForm(request.POST)
        if form.is_valid():
            new_course = Course(name=form.cleaned_data["course_name"], short_desc=form.cleaned_data["short_desc"],
                                description=form.cleaned_data["desc"], instructor=form.cleaned_data["instructor"],
                                duration=form.cleaned_data["duration"],
                                delivery_mode=form.cleaned_data["delivery_mode"],
                                keywords=form.cleaned_data["keywords"], date_added=date.today().isoformat(),
                                date_updated=date.today().isoformat())
            new_course.save()
    return render(request, "Courses/new_course_with_form.html", {'form': form})


def my_search_view(request):
    if request.method == 'GET':
        return render(request, "Courses/my_search.html")


def show_all_courses(request):
    if request.method == "GET":
        all_courses = Course.my_courses.all()
    return render(request, "Courses/show_all_courses.html", {'all_courses': all_courses})


def new_course_using_model_form(request):
    if request.method == "POST":
        form = NewCourseFormUsingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("courses_show_all_courses"))
    elif request.method == "GET":
        form = NewCourseFormUsingModelForm()
    return render(request, "Courses/new_course_with_model_form.html", {'form': form})



class ShowAllCourses(View):
    template_name = 'Courses/show_all_courses.html'

    def get(self, request, *args, **kwargs):
        all_courses = Course.my_courses.all()
        return render(request, self.template_name, {'all_courses': all_courses})


class AddNewCourseUsingModelForm(View):
    form_class = NewCourseFormUsingModelForm
    template_name = 'Courses/new_course_with_model_form.html'

    def get(self, request, *args, **kwargs):
        form = NewCourseFormUsingModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("courses_view_class_all_courses"))
        return render(request, self.template_name, {'form': form})



class ShowAllCourseListView(ListView):
    model = Course
    context_object_name = 'all_courses'
    ordering = ['name']
    queryset = Course.my_courses.all()
    template_name = 'Courses/show_all_courses.html'


class AddNewCourseCreateView(CreateView):
    model = Course
    context_object_name = 'course'
    fields = ['name', 'short_desc', 'description', 'instructor', 'duration', 'delivery_mode', 'keywords']
    success_url = reverse_lazy('courses_view_class_all_courses')

    def form_valid(self, form):
        if form.instance.duration < 10 or form.instance.duration > 120:
            form.add_error('duration', 'duration must be between 10 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


'''

from django.views.generic import CreateView
class AddNewCourseCreateView(CreateView):
    context_object_name = 'course'
    form_class = NewCourseFormUsingModelForm
    template_name = 'Courses/course_form.html'
    success_url = reverse_lazy('courses_view_class_all_courses')

    def form_valid(self, form):
        if form.instance.duration < 10 or form.instance.duration > 120:
            form.add_error('duration', 'duration must be between 10 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)
'''



class CourseUpdateView(UpdateView):
    model = Course
    context_object_name = 'course'
    fields = ['name', 'short_desc', 'description', 'instructor', 'duration', 'delivery_mode', 'keywords']
    success_url = reverse_lazy('courses_view_class_all_courses')

    def form_valid(self, form):
        # print("Self.object = ", self.object.name, self.object.short_desc,self.object.description, self.object.instructor,
        # self.object.duration, self.object.delivery_mode, self.object.keywords)
        # print("form.instance = ", form.instance.name, form.instance.short_desc, form.instance.description, form.instance.instructor,
        # form.instance.duration, form.instance.delivery_mode, form.instance.keywords)
        # print("form.initial = ", form.initial)
        # print("form.cleaned_data = ", form.cleaned_data)
        if form.instance.duration < 10 or form.instance.duration > 120:
            form.add_error('duration', 'duration must be between 10 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


'''
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses_view_class_all_courses')
'''


class AddNewCourse(LoginRequiredMixin, CreateView):  # Updated line
    context_object_name = 'course'
    form_class = NewCourseFormUsingModelForm
    template_name = 'Courses/course_form.html'
    success_url = reverse_lazy('courses_index_page')


from django.contrib import messages
@login_required
def add_new_course(request):
    if request.method == "POST":
        print(request.POST)
        form = NewCourse(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.course_active_status == 'A':
                obj.course_active_on = date.today().isoformat()
            elif obj.course_active_status == 'I':
                obj.course_active_on = None
            obj.save()
            messages.success(request, f"New course on {obj.course_name} is now available") # New change here.
            return HttpResponseRedirect(reverse("courses_index_page"))
    elif request.method == "GET":
        form = NewCourse()
    return render(request, "courses/add_new_course.html", {'form': form})