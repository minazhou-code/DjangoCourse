from django.urls import path
from . import views

urlpatterns = [
    # path('view_class/<int:pk>/course_delete_view/', views.CourseDeleteView.as_view(), name='courses_view_class_delete_Course_with_delete_view'),
    path('view_class/<int:pk>/course_update_view/', views.CourseUpdateView.as_view(),name='courses_view_class_update_Course_with_update_view'),
    path('view_class/add_new_with_create_view/', views.AddNewCourseCreateView.as_view(), name='courses_view_class_add_new_with_create_view'),
    path('view_class_with_list_view/all_courses/', views.ShowAllCourseListView.as_view(), name='courses_view_class_with_list_view_all_courses'),
    path('view_class/add_new/', views.AddNewCourseUsingModelForm.as_view(),name='courses_view_class_add_new'),
    path('view_class/all_courses/', views.ShowAllCourses.as_view(), name='courses_view_class_all_courses'),
    path('', views.show_all_courses, name='courses_show_all_courses'),
    path('new_course_with_model_form/', views.new_course_using_model_form, name='courses_new_course_using_model_form'),
    path('new_course_with_form/', views.new_course_using_form, name='courses_new_course_with_form'),
    path('new_course/',views.new_course,name='courses_new_course'),
    path('sample_form/', views.sample_form_view, name='courses_sample_form'),
    path('search/', views.my_search_view, name='courses_search'),
]