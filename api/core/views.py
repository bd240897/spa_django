from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, ContactSerailizer, RegisterSerializer, UserSerializer, CommentSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import pagination
from .serializers import TagSerializer
from taggit.models import Tag
from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from django.core.mail import send_mail
from .models import Comment
import urllib.parse

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

    # ДЛЯ РАБОЫТ ПОИСКА - библа сама лезет в таблицу (не гибкий)
    # поиск по этим полям
    search_fields = ['$content', '$h1']
    # фильтр поиска
    filter_backends = (filters.SearchFilter,)

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
        # tag_slug = self.kwargs['tag_slug'].lower()
        # tag = Tag.objects.get(slug=tag_slug)
        # return Post.objects.filter(tags=tag)
        # TODO почему то отправляется название тега а не слаг из vue
        tag_slug = urllib.parse.unquote(self.kwargs['tag_slug'])
        return Post.objects.filter(tags__name=tag_slug)

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

class FeedBackView(APIView):
    """Вьюха формы обратнйо связи"""
    # аналог Class Based View

    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerailizer

    def post(self, request, *args, **kwargs):
        #  наша апишка будет принимать данные только на вход

        # сохраним данные которые нам пришли с фронта
        serializer_class = ContactSerailizer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get('name')
            from_email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            # TODO ascii cant encode
            # send_mail('<Your subject>', '<Your message>', 'from@example.com', ['to@example.com'])
            # send_mail(u'1111111111', u'message', u"from_email", [u'dima@mail.com'])
            # from django.core.mail.message import EmailMessage
            # msg = EmailMessage(
            #     u"Wymagane zresetowanie hasła do GSMtasks",
            #     u"Kliknij aby zresetować hasło",
            #     u'from@example.com', [u'to@example.com'])
            # msg.send()
            print("data", data)
            return Response({"success": "Sent"})
        print("data", request.data)
        return Response({"error": "some problem with data"}, status=400)

class RegisterView(generics.GenericAPIView):
    """Регистрация"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # в ответ вкладываем данные о только что созданном пользователе. context=self.get_serializer_context() - что это, какой то доп контекст
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
        })

class ProfileView(generics.GenericAPIView):
    """Профиль пользователя"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args,  **kwargs):
        "Только гет запросы"
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })

class CommentView(generics.ListCreateAPIView):
    """Вью комментариев сразу на get и post"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # получение поределенного поста -  эндпойнт - http://localhost:8000/api/comments/<post_slug>/
        post_slug = self.kwargs['post_slug'].lower()
        post = Post.objects.get(slug=post_slug)
        return Comment.objects.filter(post=post)

class TestView(generics.GenericAPIView):
    """Профиль пользователя"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args,  **kwargs):
        "Только гет запросы"
        return Response({"massage": "good"}, status=404)



############
# в чем разница ?
# viewsets.ModelViewSet
# generics.ListAPIView
# APIView - обычная вьха где есть get и post
# generics.GenericAPIView
# generics.ListCreateAPIView

# https://habr.com/ru/company/yandex_praktikum/blog/561696/