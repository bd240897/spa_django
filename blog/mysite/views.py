from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class FirstView(View):
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Все хорошо')
    #
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'mysite/home.html'
        )