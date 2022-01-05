from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    pass

# регистрация нашей модели в админке
admin.site.register(Post, PostAdmin)