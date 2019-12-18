from django.db import models

# Create your models here.

class Projects(models.Model):
    """Displays list of projects worked on the protfolio site."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/")

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class BackgroundImage(models.Model):
    """Homepage background image"""
    bg_image = models.ImageField(upload_to="bg images")

    class Mwta:
        verbose_name_plural = "Background Images"

class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name_plural = "About Me"
    
    def __str__(self):
        return self.about

        