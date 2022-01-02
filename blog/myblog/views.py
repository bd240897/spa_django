from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from django.core.paginator import Paginator

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
        return render(request, 'myblog/post_detail.html', context={
            'post': post
    })