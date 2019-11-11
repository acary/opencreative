from django.shortcuts import render, get_object_or_404
from .models import Highlight

def highlight_index(request):
    posts = Highlight.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "highlight_index.html", context)

def highlight_detail(request,pk):
    post = Highlight.objects.get(pk=pk)
    context = {
        "detail": post.detail,
        "image": post.image,
        "caption": post.caption,
        "created_on": post.created_on,
        "link": post.link,
    }
    return render(request, "highlight_detail.html", context)
