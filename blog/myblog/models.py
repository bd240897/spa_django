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

class Comment(models.Model):
    """Модель для комментариев"""
    # связь один-ко-многим, related_name - для QS по связанным таблицам - Post.objects.get(url=slug).comments.all()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # связь один-ко-многим
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    # ля сортировки комментариев.
    class Meta:
        ordering = ['-created_date']

    # для админки
    def __str__(self):
        return self.text