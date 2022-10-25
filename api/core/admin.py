from django.contrib import admin
from .models import Post
from taggit.models import Tag


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("get_image",)
    #
    # def get_image(self, obj):
    #     return Tag.objects.all()
    pass

# регистрация нашей модели в админке
admin.site.register(Post, PostAdmin)