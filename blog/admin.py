from django.contrib import admin
from .models import Category, Post, Comment
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
"""class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"

class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
"""
class PostAdmin(admin.ModelAdmin):

    """Overides normal text input field to an html text input field"""
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
class CategoryAdmin(admin.ModelAdmin):
    """Overides normal text input field to an html text input field"""
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)