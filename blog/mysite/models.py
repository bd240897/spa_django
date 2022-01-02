from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# модель блога
class Achieve(models.Model):
    name = models.CharField(max_length=200)
    data_start = models.DateField(blank=True, default=timezone.now)
    data_stop = models.DateField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    certificate = models.ImageField(blank=True, null=True)

    def __str__(self):
        # для отображения в админке
        return self.name