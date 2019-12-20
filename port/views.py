from django.shortcuts import render
from .models import Projects, BackgroundImage, AboutMe
import datetime


# Create your views here.
def home(request):
    image = ""
    try:
        images = BackgroundImage.objects.all().order_by("-id")[0]
        image = images
    except :
        pass
    projects = Projects.objects.all()
    #getting year for footer copyright year
    t = datetime.datetime.now()
    return render(
        request = request,
        template_name = 'port/home.html',
        context = {
            "image": image,
            "projects": projects,
            "year": t.year
        
        }
    )
def project_detail(request, pk):
    details = Projects.objects.get(pk=pk)
    #getting year for footer copyright year
    t = datetime.datetime.now()
    return render(
        request, "port/details.html", {"details": details, "year": t.year}
    )
def about_me(request):
    about = AboutMe.objects.all()[0]
    t = datetime.datetime.now()
    return render(
        request,
        "port/about.html",
        {
            "about": about,
            "year": t.year
        }
    )
def contact(request):
    t = datetime.datetime.now()
    return render(
        request,
        "port/contact.html",
        {
            "year": t.year
        }
    )
