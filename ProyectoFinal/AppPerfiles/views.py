from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"Home.html",{"mensaje":f"Bienvenido {username}"})

        else:
            return render(request,"Login.html",{"mensaje":f"Ingresaste datos incorrectos"})
        # Return an 'invalid login' error message.
    else:
        return render(request,"Login.html",{})

@login_required
def editarPerfil(request):
    
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.set_password(informacion["password1"])
            usuario.save()

            return render(request, "Home.html",{"mensaje":"Tus datos han sido actualizados"})

    else:

        miFormulario = UserEditForm(instance = request.user)

    return render(request, "Profile.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def crearblog(request):
    if request.method == 'POST':
        miFormulario = editBlog(request.POST, request.FILES)
        if miFormulario.is_valid():
            data = User.objects.get(username = request.user)
            data2 = miFormulario.cleaned_data
            blog = blogs(user=data,tituloBlog = data2['tituloBlog'],textoBlog=data2['textoBlog'],imagen=data2['imagen'])
            blog.save()
            return render(request, "Home.html")
        else:
            return render(request, "Home.html",{"mensaje": "Formulario Invalido"})
    else:
        miFormulario =editBlog()
        return render(request, "CreateBlog.html", {"miFormulario": miFormulario })


@login_required
def EliminarBlog(request):
    Blogs = blogs.objects.get()
    Blogs.delete()
    return render(request,"Home.html")

@login_required
def mostrar_Blog(request):
    Blogs = blogs.objects.get(user=request.user.id)
    BlogTexto = blogs.objects.get()
    BlogTitulo = blogs.objects.get()
    
    return render(request,"GetMiBlog.html",{'url' : Blogs.imagen.url,'texto': BlogTexto.textoBlog,'titulo':BlogTitulo.tituloBlog})

@login_required
def editar_blog(request, id_blog):
       # Recibe el nombre del profesor que vamos a modificar
    blog = blogs.objects.get(id=id_blog)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = editBlog(request.POST,request.FILES)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            blog.tituloBlogs = informacion['tituloBlog']
            blog.email = informacion['textoBlog']
            blog.profesion = informacion['imagen']
            blog.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "Home.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = editBlog(initial={ 'tituloBlog': blog.tituloBlogs,
                                    'textoBlog': blog.email, 'imagen': blog.profesion})

    # Voy al html que me permite editar
    return render(request, "UpdateBlog.html", {"miFormulario": miFormulario, "id_blog": id_blog})


def verEdit(request):
    return render(request,"UpdateBlog.html")

def verElim(request):
    return render(request,"DeleteBlog.html")


