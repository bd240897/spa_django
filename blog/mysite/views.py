from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Achieve
from django.core.paginator import Paginator
from django.db.models import Q

class HomeView(View):
    "Вьюха главной страницы"
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Все хорошо')
    #
    def get(self, request, *args, **kwargs):
        return render(request,'mysite/home.html')

class AchievementsView(View):
    "Вьюха страницы достижений"

    # def get(self, request, *args, **kwargs):
    #     return render(request,'mysite/achievements.html')

    def get(self, request, *args, **kwargs):
        achieves = Achieve.objects.order_by('-data_start')
        paginator = Paginator(achieves, 3)
        # номер страницы
        page_number = request.GET.get('page')
        achieves_obj = paginator.get_page(page_number)
        return render(request, 'mysite/achievements.html', context={'achieves_obj': achieves_obj})

class AchievementDetailsView(View):
    "Вьюха ПОДБРОБНОСТИ страницы достижений"

    # def get(self, request, *args, **kwargs):
    #     return render(request,'mysite/achievements.html')

    def get(self, request, id, *args, **kwargs):
        achieve = get_object_or_404(Achieve, id=id)
        # print('121312312', achieve.benefit == '')
        return render(request, 'mysite/achievements_detail.html', context={'achieve': achieve})


class СontactsView(View):
    "Вьюха страницы контактов"

    def get(self, request, *args, **kwargs):
        return render(request,'mysite/сontacts.html')

class SearchAchieveView(View):
    """Вьюха поиска по достижениям - только метод get"""

    def get(self, request, *args, **kwargs):
        # вытаскиваем парметры из азпроса
        query = self.request.GET.get('q')
        # icontains не может работать с None.
        results = ""
        if query:
            # сам QuerySet - по полю h1 или полю content
            QuerySet = Q(name__icontains=query) | Q(description__icontains=query) | Q(list_studied__icontains=query) | Q(benefit__icontains=query)
            results = Achieve.objects.filter(QuerySet)
        # пагинация
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'mysite/search_achievement.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })

