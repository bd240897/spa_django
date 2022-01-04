from django.urls import path
from .views import HomeView, AchievementsView, СontactsView, AchievementDetailsView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('contacts/', СontactsView.as_view(), name='contacts'),
    path('achievements/<id>/', AchievementDetailsView.as_view(), name='achievements_detail'),
]