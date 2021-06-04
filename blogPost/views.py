from django.contrib.auth import models
from django.shortcuts import render, redirect
from .models import Article, Comentario
from django.contrib import messages
from django.views import generic

class postListView(generic.ListView):
    model = Article
    paginate_by = 2
    template_name = "index.html"

def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

def contenido(request,post):
    if request.method == "POST": 
        text = request.POST["text"]
        try:
            comentario = Comentario(user = request.user,article = Article.objects.get(id = post),text=text)
            articulo= Article.objects.get(id = post)
            articulo.comentarios = articulo.comentarios + 1 
            articulo.save()
            comentario.save()
        except:
            messages.info(request,"Para dejar un comentario registrate o inicia sesión si ya estás registrado.")
        return redirect("/" + str(post))
    else:
        try:
            yo = request.user.username
        except:
            yo = ""
        vacio = False
        consulta = Article.objects.get(id = post)
        comentarios = Comentario.objects.filter(article = consulta)
        if len(comentarios) < 1:
            vacio = True
        return render(request,"post.html",{"consulta":consulta,"comentarios":comentarios,"vacio":vacio,"yo":yo})
