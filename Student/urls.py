from django.urls import path
from . import views

urlpatterns = [
    #. . .
    path('read_cookies/', views.read_cookies, name='student_read_cookies'),
    path('set_new_secret_cookie/', views.set_a_new_secret_cookie, name='student_set_a_new_secret_cookie'),
    path('session_details/', views.get_session_details, name='student_session_details'),
    path('add_to_session/', views.set_session_details, name='student_add_to_session'),
    path('encrypt_cookie/', views.encrypt_cookie, name='encrypt_cookie'),
]