from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post, Comment

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"

class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)