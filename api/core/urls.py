from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagDetailView, TagView

# переменную router и сохранили в нее DefaultRouter - БЕРЕТ ВСЮ РАБОТУ НА СЕБЯ
router = DefaultRouter()
# арегистрировали url до нашей вьюхи PostViewSet
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    # добавили пути содержащиеся в роутере в список urlpatterns
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
]