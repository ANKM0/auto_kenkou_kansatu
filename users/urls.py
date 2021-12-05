from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView


urlpatterns = [
    # ホーム
    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowtoView.as_view(), name='howto'),
    # path('linelogin/', views.LineLogin.as_view(), name='linelogin'),
    # path('accounts/', include('allauth.urls')),
    # path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),

    path('', include('social_django.urls', namespace='social')),  # 追加
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # 追加
    # # 詳細画面
    # path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # # 登録画面
    # path('create/', ItemCreateView.as_view(), name='create'),
    # # 更新画面
    # path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # # 削除画面
    # path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]
