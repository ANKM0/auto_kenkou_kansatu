from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # ホーム
    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowtoView.as_view(), name='howto'),

    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),

    path('input/', views.input, name='input'),
    path('output/', views.output, name='output'),

    path('', include('social_django.urls', namespace='social')),  # 追加
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # 追加

    path("item", views.ItemCreateView.as_view(), name='item'),

    # 詳細画面
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', views.ItemCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),

]
