
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.list_posts, name='blogs_list_posts'),
    # path('page_view/', views.PostListsView.as_view(), name='blogs_list_posts_page_view'),
    path('page_view/', views.post_list_view_func_with_pagination, name='blogs_list_posts_page_view'),
    # path('add_new_post/', views.AddNewPost.as_view(), name='blogs_add_new_post'),
    # path('review_post/', views.ReviewPost.as_view(), name='blogs_review_post'),
    # path('post/<slug:slugss>/', views.PostDetailView.as_view(), name='show_post'),
]