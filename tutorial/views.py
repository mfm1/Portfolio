from django.shortcuts import render, redirect
from .models import Post, Category, Comments
from .forms import CommentForm
import datetime
# Create your views here.
def tutorial_home(request):
    #getting year for footer copyright year
    t = datetime.datetime.now()
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
        "year": t.year
    }
    return render(
        request, "tutorial/tutorial_home.html", context
    )

def tutorial_category(request, category):
    categories = Category.objects.filter(name = category)
    #getting year for footer copyright year
    t = datetime.datetime.now()
    return render(
        request, "tutorial/tutorial_category.html", {"categories": categories, "year":t.year}
    )
def tutorial_detail(request, pk):
    post = Post.objects.get(pk=pk)
    #getting year for footer copyright year
    t = datetime.datetime.now()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
            return redirect("tutorial:details", post.pk)

    comments = Comments.objects.filter(post=post).order_by("-created_on")


    return  render(
        request, "tutorial/tutorial_detail.html", 
        {"post": post, "comments": comments, "form": form, "year": t.year}
    )

