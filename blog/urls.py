from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from usuario import views as usuario_view

urlpatterns = [

    # Home
    #path("", views.listado_nineras, name="home"),
    path("", views.listado_post, name="home"),

    # 404
    path("page404/", views.page404, name="page404"),

    # Usuario
    path("registrarninera/", usuario_view.registrar_ninera, name="registrar_ninera"),
    path("registrarcliente/", usuario_view.registrar_cliente, name="registrar_cliente"),

    # Redirección de login
    path("profileninera/", usuario_view.profile_ninera, name="profile_ninera"),
    path("profilecliente/", usuario_view.profile_cliente, name="profile_cliente"),

    # path("profileninera/", views.crear_hoja_vida, name="crear_hoja_vida"),


    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    # path("", views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

