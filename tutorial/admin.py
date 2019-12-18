from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comments

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"

class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
