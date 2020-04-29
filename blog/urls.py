from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from usuario import views as usuario_view

from django.contrib.auth import views as auth_views

urlpatterns = [

    # Home
    #path("", views.listado_nineras, name="home"),
    path("", views.listado_post, name="home"),

    # 404
    path("page404/", views.page404, name="page404"),

    # Políticas
    path("tyc/", views.tyc, name="tyc"),
    path("cookies/", views.cookies, name="cookies"),
    path("avisolegal/", views.avisolegal, name="avisolegal"),
    path("acerca_de/", views.acerca_de, name="acerca_de"),

    # password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),

    # Usuario
    path("registrarninera/", usuario_view.registrar_ninera, name="registrar_ninera"),
    path("registrarcliente/", usuario_view.registrar_cliente, name="registrar_cliente"),

    # Redirección de login
    path("profileninera/", usuario_view.profile_ninera, name="profile_ninera"),
    path("profilecliente/", usuario_view.profile_cliente, name="profile_cliente"),

    # Modificar perfil niñera
    path("modificar_publicacion/<id>/", usuario_view.modificar_publicacion, name="modificar_publicacion"),

    # path("profileninera/", views.crear_hoja_vida, name="crear_hoja_vida"),


    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    # path("", views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]