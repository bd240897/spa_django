from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagDetailView, TagView, AsideView, FeedBackView, RegisterView, ProfileView, CommentView, \
    TestView

# переменную router и сохранили в нее DefaultRouter - БЕРЕТ ВСЮ РАБОТУ НА СЕБЯ
router = DefaultRouter()
# арегистрировали url до нашей вьюхи PostViewSet
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    # добавили пути содержащиеся в роутере в список urlpatterns
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<str:tag_slug>/", TagDetailView.as_view()),
    path("aside/", AsideView.as_view()),
    path("feedback/", FeedBackView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("comments/", CommentView.as_view()), # для создания
    path("comments/<slug:post_slug>/", CommentView.as_view()), # для получение
    path("test/", TestView.as_view()), # для получение
]