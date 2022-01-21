# мы импортировали объект serializers внутри которого находятся различные вариации сериалайзеров.
# ModelSerializer - сериализация на основе модели.
from rest_framework import serializers
from .models import Post
# сериализаторы для тегов
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User
from taggit.models import Tag

# Сюрриализация - достать данные из БД, а затем преобразовать их в формат JSON. Этот процесс называется сериализацией.
# будем преобразовывать экземпляры моделей в JSON и наоборот.

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """сериализатор БД поста - аналог создания формы на основе омдели"""

    # ПОЛЯ

    #  добавить поле TagListSerializerField()
    tags = TagListSerializerField()
    # получение именя по связаной модели - без этого выдаст нам id а не username (вложенные отношения)
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        """на какой модели основан сериализатор"""
        model = Post
        # какие поля нам нужны из модели
        fields = ("id", "h1", "title", "slug", "description", "content", "image", "created_at", "author", "tags")
        # по какому полю мы будем получать конкретную запись, можно по id по умолчанию
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

# КАК РАБОТАЕТ - url - view - serializers - BD - JSON
# сериализатор берет из БД данные и в соответствии с настройками сериализатора, возвращает нам данные в виде JSON.

class TagSerializer(serializers.ModelSerializer):
    """Серюлиазатор для списка тегов"""

    class Meta:
        model = Tag
        fields = ("name",)
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }

class ContactSerailizer(serializers.Serializer):
    """Форма братной свящи"""

    name = serializers.CharField()
    email = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()