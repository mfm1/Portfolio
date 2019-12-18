from django.shortcuts import render, redirect
from .models import Category, Post, Comment
from .forms import CommentForm
import datetime

# Create your views here.
def blog_home(request):
    content = Post.objects.all().order_by("-created_on")
    #getting year for footer copyright year
    t = datetime.datetime.now()
    return render(
        request, "blog/blog_home.html", {"contents": content, "year": t.year}
    )

def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    #getting year for footer copyright year
    t = datetime.datetime.now()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
            return redirect(
                "blog:details", post.pk
            )

    comments = Comment.objects.filter(post=post)


    return  render(
        request, "blog/blog_details.html", 
        {"post": post, "comments": comments, "form": form, "year": t.year}
    )

def blog_category(request, category):

    categories = Category.objects.filter(name = category)
    #getting year for footer copyright year
    t = datetime.datetime.now()
    return render(
        request, "blog/blog_category.html", {"categories": categories, "year": t.year}
    )