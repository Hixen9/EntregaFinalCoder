from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/",login_request,name ="Login"),
    path("logout/", LogoutView.as_view(template_name='Logout.html'),name = 'Logout'),
    path("miperfil/",editarPerfil,name="Profile"),
    path("Miblog/", mostrar_Blog,name="GetMiBlog"),
    path("eliminar/",EliminarBlog,name ="Eliminar"),
    path("editblog/",verEdit,name="EditBlog"),
    path("crearblog/",crearblog,name="CreateBlog"),
    path("editblog/<int:id_blog>",editar_blog,name="EditBlog2"),
    path("viewEliminar/",verElim,name="ViewEliminar")
]
