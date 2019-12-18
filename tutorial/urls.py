from django.urls import path
from . import views

app_name = "tutorial" # for namespacing

urlpatterns = [
    path('', views.tutorial_home, name='home'),
    path('<int:pk>/', views.tutorial_detail, name='details'),
    path('<category>/', views.tutorial_category, name='category')
]