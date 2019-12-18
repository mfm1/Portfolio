from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Projects, BackgroundImage, AboutMe

# Register your models here.
class ProjectsAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(AboutMe, AboutAdmin)
admin.site.register(BackgroundImage)