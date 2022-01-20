from django.urls import path
from .views import HomeView, AchievementsView, СontactsView, AchievementDetailsView, SearchAchieveView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('contacts/', СontactsView.as_view(), name='contacts'),
    path('achievements/<id>/', AchievementDetailsView.as_view(), name='achievements_detail'),
    # поиск по достижениниям
    path('search_achievement/', SearchAchieveView.as_view(), name='search_achievement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)