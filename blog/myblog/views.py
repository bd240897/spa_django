from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from django.core.paginator import Paginator
from .forms import SigUpForm, SignInForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import FeedBackForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from taggit.models import Tag
from .forms import CommentForm
from .models import Comment

class MainView(View):
    """Вьюха главной страницы"""
    # def get(self, request, *args, **kwargs):
    #     return render(
    #         request,
    #         'myblog/home.html'
    #     )

    # def get(self, request, *args, **kwargs):
    #     posts = Post.objects.all()
    #     return render(request, 'myblog/home.html', context={
    #         'posts': posts
    #     })

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        # номер страницы
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'myblog/home.html', context={
            'page_obj': page_obj
        })

class PostDetailView(View):
    """Вьюха поста"""

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        common_tags = Post.tag.most_common()
        last_posts = Post.objects.all().order_by('-id')[:3]
        # форма комментариев
        comment_form = CommentForm()
        return render(request, 'myblog/post_detail.html', context={
            'post': post,
            'common_tags': common_tags,
            'last_posts': last_posts,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        # проверка на валидность
        if comment_form.is_valid():
            # создание коммента
            text = request.POST['text']
            # сохраняем username авторизированного пользователя, если он не авторизирован, то сохранится None
            username = self.request.user
            # сохраняем наш пост.
            post = get_object_or_404(Post, url=slug)
            # сохраняем в БД
            comment = Comment.objects.create(post=post, username=username, text=text)
            # редирект на адрес источник запроса
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'myblog/post_detail.html', context={
            'comment_form': comment_form
        })

class SignUpView(View):
    """Вьха формы регистрации"""

    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):

        # принимаем данные
        form = SigUpForm(request.POST)

        # проверяем форму на валидность.
        if form.is_valid():
            # метод описан в форму - возвращает нам authenticate пользователя
            user = form.save()
            if user is not None:
                # залогиним пользователя
                login(request, user)
                # редирект на главную страницу
                return HttpResponseRedirect('/myblog')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })

class RedirectTest(View):
    """RedirectTest"""

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/myblog')

class SignInView(View):
    """Форма входа"""

    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/myblog')
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })

class FeedBackView(View):
    """Вьюха контактов - написать мне"""

    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'myblog/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                # ошибка тут from_email - принадлежит мне - я там должен генерить ключ!!!
                send_mail(f'От {name} | {subject}', message, from_email, ['bd240897@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            # используем короткое имя success
            return HttpResponseRedirect('success')
        return render(request, 'myblog/contact.html', context={
            'form': form,
        })

class SuccessView(View):
    """Вью страницы спасибо"""

    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/success.html', context={
            'title': 'Спасибо'
        })

class SearchResultsView(View):
    """Вьюха поиска по статьям"""

    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/search.html', context={
            'title': 'Поиск'
        })


class SearchResultsView(View):
    """Вьюха поиска - только метод get"""

    def get(self, request, *args, **kwargs):
        # вытаскиваем парметры из азпроса
        query = self.request.GET.get('q')
        # icontains не может работать с None.
        results = ""
        if query:
            # сам QuerySet - по полю h1 или полю content
            results = Post.objects.filter(
                Q(h1__icontains=query) | Q(content__icontains=query)
            )
        # пагинация
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })


class TagView(View):
    """Обрабокта тегов"""

    def get(self, request, slug, *args, **kwargs):
        # вытаскиваем тег по слагу - Tag - импортунли из библы
        tag = get_object_or_404(Tag, slug=slug)
        # ищем посты с тегом
        posts = Post.objects.filter(tag=tag)
        # не работает в новой Django - pip install --upgrade Django==3.2.11
        common_tags = Post.tag.most_common()
        return render(request, 'myblog/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })