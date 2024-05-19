from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound
import datetime
from .models import Post, Author
from .forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import permission_required


# Create your views here.
def test(request, post_id=0):
    # print("test view")
    print(post_id, type(post_id))
    t = datetime.datetime.now()
    return render(request, "test.html", {"current_time":t})

def show_posts(request):
    posts = Post.objects.all()
    vp = request.session.get('vp', [])
    return render(request, "posts.html", {"posts":posts, "vp":vp})

def show_post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
        vp = request.session.get('vp', [])
        if post_id not in vp:
            vp.append(post_id)
            request.session['vp'] = vp
    except:
        return HttpResponseNotFound("<h1>404 - Post not found</h1>")

    return render(request, "post.html", {"post":p})

@permission_required('main.add_post')
def add_post(request):

    if request.method == 'POST':
        add_post_form = AddPostModelForm(request.POST, request.FILES)

        if add_post_form.is_valid():
            # post_entry = Post()
            # post_entry.author = Author.objects.all()[0]
            # post_entry.issued = datetime.datetime.now()
            # post_entry.title = add_post_form.cleaned_data['title']
            # post_entry.content = add_post_form.cleaned_data['content']
            # post_entry.post_type = add_post_form.cleaned_data['post_type']
            # post_entry.image = add_post_form.cleaned_data['image']

            # post_entry.save()

            post_entry = add_post_form.save(commit=False)
            post_entry.author = Author.objects.get(email=request.user.email)
            post_entry.issued = datetime.datetime.now()

            add_post_form.save()

            add_post_form.save_m2m()

            return redirect('post', post_entry.id)



    else:
        add_post_form = AddPostModelForm()

    return render(request, "add_post.html", {'form':add_post_form})