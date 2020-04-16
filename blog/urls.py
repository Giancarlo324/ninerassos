from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from usuario import views as usuario_view

urlpatterns = [

    # Usuario
    path("registrarninera/", usuario_view.registrar_ninera, name="registrar_ninera"),
    path("registrarcliente/", usuario_view.registrar_cliente, name="registrar_cliente"),


    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

