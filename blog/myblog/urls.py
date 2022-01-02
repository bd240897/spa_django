from django.urls import path
from .views import MainView, PostDetailView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('<slug>/', PostDetailView.as_view(), name='post_detail'),
]