import email
from turtle import title
from django.shortcuts import render

from blog.models import Category, Post, Subscribers
from blog.utils import addSubscribers
from blog.views import category


# Create your views here.
def frontpage(request):
    query = request.GET.get("query", "")
    addSubscribers(request.GET.get("email", ""))
        
    posts = Post.objects.filter(category__title__icontains=query)
    categories = Category.objects.exclude(title="All")
    category_all = Category.objects.get(id=6)

    context = {
        "posts" : posts,
        "categories" : categories,
        "category_all": category_all
    }
    return render(request, "core/index.html", context)


