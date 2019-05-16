from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Generic class for discrete written items in a blog.

    Pretty self explanatory, right?


    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Act of pushing a post to database and website.

        Any questions?

        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Summary here.

        Detail here.

        """
        return self.title
