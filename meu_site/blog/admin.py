from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = ('título', 'autor','publicado','status')
    search_fields = ('título','conteúdo')
    prepopulated_fields = {'slug':('título',)}
    list_filter = ('título','criado','publicado','autor')
    date_hierarchy = 'publicado'