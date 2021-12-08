from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from.apps import UserConfig


APP_LABEL_USER = UserConfig.name

urlpatterns = [
    # ホーム
    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowtoView.as_view(), name='howto'),

    path('', include('social_django.urls', namespace='social')),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("create/", views.UserInfoCreateView.as_view(), name="create"),
    path("list/", views.UserInfoListView.as_view(), name="list"),
    path("update/<int:pk>/", views.UserInfoUpdateView.as_view(), name="update"),
]
