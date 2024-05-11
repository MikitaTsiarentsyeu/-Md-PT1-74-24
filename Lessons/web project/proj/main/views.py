from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound
import datetime
from .models import Post, Author
from .forms import AddPost

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

def add_post(request):

    if request.method == 'POST':
        add_post_form = AddPost(request.POST, request.FILES)

        if add_post_form.is_valid():
            post_entry = Post()
            post_entry.author = Author.objects.all()[0]
            post_entry.issued = datetime.datetime.now()
            post_entry.title = add_post_form.cleaned_data['title']
            post_entry.content = add_post_form.cleaned_data['content']
            post_entry.post_type = add_post_form.cleaned_data['post_type']
            post_entry.image = add_post_form.cleaned_data['image']

            post_entry.save()

            return redirect('post', post_entry.id)



    else:
        add_post_form = AddPost()

    return render(request, "add_post.html", {'form':add_post_form})