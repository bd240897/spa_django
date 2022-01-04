from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, RedirectTest, FeedBackView, SuccessView, SearchResultsView
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
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    # поиск по статьям
    path('search/', SearchResultsView.as_view(), name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)