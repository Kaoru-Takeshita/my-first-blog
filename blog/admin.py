# from django.contrib import admin

# Register your models here.
#以下が追加のコード
from django.contrib import admin
from .models import Post

admin.site.register(Post)