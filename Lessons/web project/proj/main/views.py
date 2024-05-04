from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
import datetime
from .models import Post, Author

# Create your views here.
def test(request, post_id=0):
    # print("test view")
    print(post_id, type(post_id))
    t = datetime.datetime.now()
    return render(request, "test.html", {"current_time":t})

def show_posts(request):
    posts = Post.objects.all()

    return render(request, "posts.html", {"posts":posts})

def show_post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        return HttpResponseNotFound("<h1>404 - Post not found</h1>")

    return render(request, "post.html", {"post":p})