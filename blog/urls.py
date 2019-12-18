from . import views 
from django.urls import path

app_name = "blog" # for namespacing

urlpatterns = [
    path('', views.blog_home, name= 'home'),
    path('<int:pk>/', views.blog_details, name= 'details'),
    path('<category>/', views.blog_category, name= 'category')
]