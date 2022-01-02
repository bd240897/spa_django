from django.contrib import admin
from .models import Achieve

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Achieve, PostAdmin)