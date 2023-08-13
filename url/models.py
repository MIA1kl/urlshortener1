from django.db import models


class UrlData(models.Model):
    url = models.CharField(max_length=200)
    shorturl = models.CharField(max_length=15)

    def __str__(self):
        return f"Short URL for: {self.url} is {self.shorturl}"
