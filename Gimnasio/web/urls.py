from django.urls import path
from . import views
from .views import (
    InscripcionListView,
    InscripcionCreateView,
    InscripcionUpdateView,
    InscripcionDeleteView,
)
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("registrarse", views.registrarse, name="registrarse"),
    path("clases", views.lista_clases, name="clases"),
    path("clase", views.crud_clase, name="crud_clase"),
    path("clase/<int:idClase>", views.crud_clase, name="crud_clase"),
    path("clase/<int:idClase>/<int:eliminar>", views.crud_clase, name="crud_clase"),
    path("socios", views.lista_socios, name="socios"),
    path("socio", views.crud_socio, name="crud_socio"),
    path("socio/<int:idSocio>", views.crud_socio, name="crud_socio"),
    path("socio/<int:idSocio>/<int:eliminar>", views.crud_socio, name="crud_socio"),
    path("profesores", views.lista_profesores, name="profesores"),
    path("profesor", views.crud_profesor, name="crud_profesor"),
    path("profesor/<int:idProfesor>", views.crud_profesor, name="crud_profesor"),
    path(
        "profesor/<int:idProfesor>/<int:eliminar>",
        views.crud_profesor,
        name="crud_profesor",
    ),
    path(
        "listado_inscripcion", InscripcionListView.as_view(), name="listado_inscripcion"
    ),
    path("alta_inscripcion", InscripcionCreateView.as_view(), name="alta_inscripcion"),
    path(
        "<int:pk>/editar_inscripcion",
        InscripcionUpdateView.as_view(),
        name="editar_inscripcion",
    ),
    path(
        "<int:pk>/eliminar_inscripcion/",
        InscripcionDeleteView.as_view(),
        name="eliminar_inscripcion",
    ),
  
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
    template_name='web/registration/password_reset.html',
    email_template_name='web/registration/password_reset_email.html',
    subject_template_name='web/registration/password_reset_subject.txt'
    ), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='web/registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='web/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='web/registration/password_reset_complete.html'), name='password_reset_complete'),
]
