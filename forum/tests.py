from django.test import TestCase
from .models import ForumPost
from django.contrib.auth.models import User


class ForumPostModelTestCase(TestCase):
    def test_str(self):
        test_user = User(first_name="Test", last_name="Testesen")
        forum_post = ForumPost(author=test_user, headline="Halla balla", content="")
        self.assertEqual(str(forum_post), "Halla balla av Test Testesen")
