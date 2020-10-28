from django.contrib import admin
from .models import Article, Comment, HashTag, Title

# Register your models here.

@admin.register(Article, Comment, HashTag, Title)
class FeedAdmin(admin.ModelAdmin):
    pass
