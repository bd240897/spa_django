from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import permissions


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