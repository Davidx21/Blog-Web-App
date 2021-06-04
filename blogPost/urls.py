from django.urls import path, re_path
from . import views

urlpatterns = [
    path("",views.postListView.as_view(), name="index"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    re_path(r'^([a-zA-Z0-9._ %+-]+)', views.contenido,  name='contenido'),
]