from django.shortcuts import render
from django.views.generic import ListView
from .models import ForumPost


class ForumPostListView(ListView):
    template_name = "forum/forum_post_list.html"
    context_object_name = "forum_posts"

    def get_queryset(self):
        return ForumPost.objects.all().order_by("-time_made")
