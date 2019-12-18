from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name= 'posts')
    
    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete= models.CASCADE)
    

    class Meta:
        verbose_name_plural = "Comments"
    
    def __str__(self):
        return self.author

