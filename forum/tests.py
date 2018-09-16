from django.test import TestCase, Client
from django.urls import reverse
from .models import ForumPost
from django.contrib.auth.models import User


class ForumPostModelTestCase(TestCase):
    def test_str(self):
        test_user = User(username="Test Testesen")
        forum_post = ForumPost(author=test_user, headline="Halla balla", content="")
        self.assertEqual(str(forum_post), "Halla balla av Test Testesen")


class ForumPostListViewTestCase(TestCase):
    def test_contains(self):
        test_user = User.objects.create(username="Test Testesen")
        ForumPost.objects.create(author=test_user, headline="Halla balla", content="kul post")
        self.client = Client()
        response = self.client.get(reverse("forum:forum_post_list"))
        self.assertContains(response, "Halla balla")
        self.assertContains(response, "av Test Testesen")
        self.assertContains(response, "kul post")

    def test_ordering(self):
        test_user = User.objects.create(username="Test Testesen")
        self.client = Client()
        post1 = ForumPost.objects.create(author=test_user, headline="Halla balla1", content="kul post")
        post2 = ForumPost.objects.create(author=test_user, headline="Halla balla2", content="kul post")
        response = self.client.get(reverse("forum:forum_post_list"))
        self.assertEquals(list(response.context["forum_posts"]), [post2, post1])
