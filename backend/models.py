from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    slug = models.SlugField(max_length=20)
    img = models.ImageField(upload_to="images/",default="images/deafult.png")

    def get_absolute_url(self):
        return reverse("blog:single", args=[self.slug])

    def __str__(self):
        return self.slug