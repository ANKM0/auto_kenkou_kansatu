from django.urls import path
from .views import AboutView, HowtoView, IndexView, InfoView
from django.contrib.auth import views as auth_views
# from . import views
# from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView


urlpatterns = [
    # ホーム
    path('', IndexView.as_view(), name='index'),
    path('howto/', HowtoView.as_view(), name='howto'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html')),
    path('about/', AboutView.as_view(), name='about'),
    path('info/', InfoView.as_view(), name='info'),
    # # 詳細画面
    # path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # # 登録画面
    # path('create/', ItemCreateView.as_view(), name='create'),
    # # 更新画面
    # path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # # 削除画面
    # path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]
