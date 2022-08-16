from turtle import title
from unicodedata import category
from django.contrib import admin
from .models import Post, Category, MailMessage, Subscribers, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' :('title',)}

    
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Subscribers)
admin.site.register(MailMessage)