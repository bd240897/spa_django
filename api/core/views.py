from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import pagination
from .serializers import TagSerializer
from taggit.models import Tag
from rest_framework import generics

class PageNumberSetPagination(pagination.PageNumberPagination):
    """Пагинация - наслед-ся от PageNumberPagination"""

    # кол-во объектов на одной странице
    page_size = 6
    # указывающее имя параметра запроса, которое позволяет клиенту устанавливать размер страницы для каждого запроса
    page_size_query_param = 'page_size'
    #  как будем сортировать посты.
    ordering = 'created_at'

class PostViewSet(viewsets.ModelViewSet):
    """Вьюха поста - модель на освное ModelViewSet, а можно на основе APIView"""
    # вью благодоря ModelViewSet - отвечает за отдачу 1 записи и нескольких записей

    # определяем сериалайзер для работы с моделью Post
    serializer_class = PostSerializer
    # определяем queryset который мы будем возвращать:
    queryset = Post.objects.all()
    # указываем поле по которому будем получать одну конкретную запись
    lookup_field = 'slug'
    # параметры доступа
    permission_classes = [permissions.AllowAny]
    # пагинация
    pagination_class = PageNumberSetPagination


class TagDetailView(generics.ListAPIView):
    """Получение записей по тегу"""

    # сер-р нам нужен JSON точно с такой же структурой и полями.
    serializer_class = PostSerializer
    # пагинация
    pagination_class = PageNumberSetPagination
    # доступ
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """Получаем пост по тегу"""

        tag_slug = self.kwargs['tag_slug'].lower()
        tag = Tag.objects.get(slug=tag_slug)
        return Post.objects.filter(tags=tag)

class TagView(generics.ListAPIView):
    """Получение списка тегов"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]

class AsideView(generics.ListAPIView):
    """Возвращает последние 5 записей"""

    queryset = Post.objects.all().order_by('-id')[:5]
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
