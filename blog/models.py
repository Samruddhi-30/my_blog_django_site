from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    E_mail = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=30)
    excerpt = models.CharField(max_length=70)
    img = models.CharField(max_length=80)
    date = models.DateField()
    content = models.TextField()
    slug = models.SlugField(default="" , null=False , unique=True)
    author = models.ForeignKey(Author , on_delete=models.CASCADE, null=False)
    tag = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title}"
