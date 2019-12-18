from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'port' #For NameSpacing

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about_me, name='about'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact')
]