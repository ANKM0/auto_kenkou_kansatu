from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve


urlpatterns = [
    # ホーム
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowtoView.as_view(), name='howto'),
    path('logout_safety/', views.LogoutSafetyView.as_view(), name='logout_safety'),


    path("create/", views.UserInfoCreateView.as_view(), name="create"),
    path("detail/<int:pk>", views.UserInfoDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.UserInfoUpdateView.as_view(), name="update"),
    # path("delete/<int:pk>/", views.UserInfoDeleteView.as_view(), name="delete"),

    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(), name="default_login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="default_logout"),
    path('guest_login/', views.guest_login, name='guest_login'),  # かんたんログイン用

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
