from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, RedirectTest
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('test/', RedirectTest.as_view(), name='redirect_test'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    # форма регистрации
    path('signup/', SignUpView.as_view(), name='signup'),
    # форма входа
    path('signin/', SignInView.as_view(), name='signin'),
    # выход используем готовый метод выхода из django
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout', ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)