from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

# from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView


urlpatterns = [
    # ホーム
    # path('', views.IndexView, name='index'),
    path('howto/', views.HowtoView.as_view(), name='howto'),
    path('', views.LineLogin.as_view(), name='linelogin'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('info/', views.InfoView.as_view(), name='info'),

    # # 詳細画面
    # path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # # 登録画面
    # path('create/', ItemCreateView.as_view(), name='create'),
    # # 更新画面
    # path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # # 削除画面
    # path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]
