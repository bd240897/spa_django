# мы импортировали объект serializers внутри которого находятся различные вариации сериалайзеров.
# ModelSerializer - сериализация на основе модели.
from rest_framework import serializers
from .models import Post
# сериализаторы для тегов
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User
from taggit.models import Tag
from django.contrib.auth.models import User
from .models import Comment

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

class RegisterSerializer(serializers.ModelSerializer):
    """Регистрация"""

    # в базе нет этого поля поэтому его добавили
    password2 = serializers.CharField(write_only=True)

    # сюр-р на основе модели
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """ Он нужен для сохранения инстансов - для создания пользователей."""

        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    """Возвращает все дпнные о пользователе"""

    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    """Комментарии"""

    # Они нам нужны для того, что в поля username возвращались не id данных объектов,  именно названия. т.к. в comments это ForeignKey
    username = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    post = serializers.SlugRelatedField(slug_field="slug", queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ("id", "post", "username", "text", "created_date")
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }