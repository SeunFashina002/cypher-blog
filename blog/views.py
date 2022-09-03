from django.db.models import Q
from blog.utils import addSubscribers
from django.shortcuts import redirect, render, get_object_or_404
from . models import Post, Category, Comment
from django.core.mail import send_mail
from .forms import MailForm

# from .forms import CommentForm

# Create your views here.

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST": 
        name = request.POST["name"]
        comment = request.POST["comments"]
        
        comm = Comment(name=name, body=comment)
        comm.post = post
        comm.save()
    
        return redirect('post_detail', category_slug=category_slug, slug=slug)

    else:
        addSubscribers(request.GET.get("email", ""))

    context = {
        "post" : post,
    }

    return render(request, "blog/detail.html", context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    context = {
        'category': category
    }
    if request.method == "GET":
        addSubscribers(request.GET.get("email", ""))
    

    return render(request, 'blog/category.html', context)

def search(request):
    query = request.GET.get("query", "")
    addSubscribers(request.GET.get("email", ""))
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(paragraph_one__icontains=query))

    context = {
        'posts': posts,
        'query': query
    }



    return render(request, 'blog/search.html', context)


# def sendMail(request):

#     if request.method == "POST":
#         form = MailForm(request.POST)
#         if form.is_valid:
#             form.save()
#             title = form.cleaned_data.get("title")
#             msg = form.cleaned_data.get("message")

#         send_mail(
#             title,
#             msg,
#             '',
#             ['akoredebakare4u@gmail.com'],
#             fail_silently=False,
#         )

#         return redirect("sendMail")

#     else:
#         form = MailForm()
        
#     context={
#         "form" : form
#     }

#     return render(request, 'blog/admin.html', context)
