from django.views import generic
from .models import Hojavida
from .forms import CommentForm, CustomUserForm, HojaVidaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from usuario.models import User
from datetime import datetime, timedelta
from django.core.paginator import Paginator


class PostList(generic.ListView):
    queryset = Hojavida.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


class NinerasList(generic.ListView):
    queryset = Hojavida.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3
    #
    #

def listado_post(request):
    postAll = Hojavida.objects.all()
    post = Hojavida.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(post, 5)
    try:
        page = int(request.GET.get('page',1))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    #

    for activo in postAll:
        #
        print("Fechaaaa finnnnnnn: "+str(activo.fecha_fin))
        print("Fecha hoyyyyyyyy: "+str(datetime.now()))
        a = int(datetime.now().strftime('%Y%m%d%H%M%S'))
        b = int(activo.fecha_fin.strftime('%Y%m%d%H%M%S'))
        print("Este es el día de hoy: "+str(a))
        print("Este es el día en que acaba: "+str(b))
        if a >= b:
            print("Cambio a sin suscripción, hoy mayor que fin")
            Hojavida.objects.filter(pk=activo.usuario.id).update(status=0)
            activo.refresh_from_db()
        else:
            print("Cambio a con suscripción, fin mayor que hoy")
            Hojavida.objects.filter(pk=activo.usuario.id).update(status=1)
            activo.refresh_from_db()
        #
    #
    data = {
        'hojavida_list': posts
    }
    return render(request, "index.html", data)


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


@login_required
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
            new_comment.active = True
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
