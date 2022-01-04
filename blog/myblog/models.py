from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# модель блога
class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField()
    # вместо models.TextField()
    description = RichTextUploadingField()
    # вместо models.TextField()
    content = RichTextUploadingField()
    # нужна библиотека pillow для работы этой библы - поле позвляет выбрать картинку с компа, генерит имя в БД и копирует саму картинку в папку media_root
    image = models.ImageField()
    #  timezone - это нам надо для фиксации времени создания поста.
    created_at = models.DateField(default=timezone.now) #
    # user - готовый класс в django для Пользователей. по умолчанию в этом поле сохраняется дата именно момента создания поста.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # теге - отдельная таблица которую создает библиотека - foreignkey
    tag = TaggableManager()

    def __str__(self):
        # для отображения в админке
        return self.title