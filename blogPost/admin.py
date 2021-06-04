from django.contrib import admin
from .models import Article, Comentario
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','autor',"date")
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('article','user',"date","time")
    search_fields = ('user',)

admin.site.register(Comentario, ComentarioAdmin)