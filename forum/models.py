from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField("Overskrift", max_length=40)
    content = models.TextField("innhold", default="")
    time_made = models.DateTimeField(default=timezone.now)
    image = models.ImageField()

    def __str__(self):
        return self.headline + " av " + self.author.first_name + " " + self.author.last_name
