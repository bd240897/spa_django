from django.urls import path
from .views import HomeView, AchievementsView, СontactsView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('contacts/', СontactsView.as_view(), name='contacts'),
]