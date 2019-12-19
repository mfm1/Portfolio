from django.contrib import admin
from .models import Projects, BackgroundImage, AboutMe
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
"""class ProjectsAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__" """
class ProjectAdmin(admin.ModelAdmin):

    """Overides normal text input field to an html text input field"""
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
class AboutAdmin(admin.ModelAdmin):
    """Overides normal text input field to an html text input field"""
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
admin.site.register(Projects, ProjectAdmin)
admin.site.register(AboutMe, AboutAdmin)
admin.site.register(BackgroundImage)