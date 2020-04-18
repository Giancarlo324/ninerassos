from django.views import generic
from .models import Hojavida
from .forms import CommentForm, CustomUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from usuario.models import User


class PostList(generic.ListView):
    queryset = Hojavida.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3

class NinerasList(generic.ListView):
    queryset = Hojavida.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3

def listado_nineras(request):
    nineras = User.objects.all()
    data = {
        'nineras': nineras
    }
    return render(request, "index.html", data)


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def page404(request):
    return render(request, '404.html')

def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Hojavida, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )