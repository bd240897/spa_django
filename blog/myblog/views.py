from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator

class MainView(View):
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