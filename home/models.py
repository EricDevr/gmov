from django.db import models
from django.utils.text import slugify

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    content = models.TextField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs): # new
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)