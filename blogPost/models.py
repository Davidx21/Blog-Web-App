from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
user = User()

class Article(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to="static/images")
    text = RichTextField(blank=True,null=True)
    date = models.DateField()
    autor = models.CharField(max_length=50)
    intro = models.TextField()
    comentarios = models.IntegerField(default=0)
    def __str__(self):
        return (str(self.title) + "_" + str(self.id))

class Comentario(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE,)
    article = models.ForeignKey('Article',on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return ("Comentario" + "_" + str(self.id) + "_" + str(self.date))