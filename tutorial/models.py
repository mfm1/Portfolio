from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        # For Admin naming
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    body = models.TextField()
    categories = models.ManyToManyField(Category, related_name="post")

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Comments(models.Model):
    author = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete = models.CASCADE)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Comments"
    
    def __str__(self):
        return self.author