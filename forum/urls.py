from django.urls import path, include
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.ForumPostListView.as_view(), name="forum_post_list"),
    ]
