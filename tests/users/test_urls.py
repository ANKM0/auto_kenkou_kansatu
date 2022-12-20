from django.test import TestCase
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from users.models import UserInfo
from users.views import IndexView, HowtoView, LogoutSafetyView, UserInfoCreateView, UserInfoDetailView, UserInfoUpdateView, guest_login


class TestUrls(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username="username", email='guestuser@example.com')
        user.save()

        object = UserInfo(
            username=user,
            user_info_grade_number=3,
            user_info_class_number=1,
            user_info_student_number=2,
            user_info_student_name="test_student_name",
            user_info_body_temperature="test_user_info_body_temperature",
        )
        object.save()

        self.object = object

    def test_logout_url(self):
        """logout ページへのURLでアクセスする時のリダイレクトをテスト"""
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_index_url(self):
        """index ページへのURLでアクセスする時のリダイレクトをテスト"""
        url = reverse('users:index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_howto_url(self):
        """howto ページへのリダイレクトをテスト"""
        url = reverse('users:howto')
        self.assertEqual(resolve(url).func.view_class, HowtoView)

    def test_logout_safety_url(self):
        """logout_safety ページへのリダイレクトをテスト"""
        url = reverse('users:logout_safety')
        self.assertEqual(resolve(url).func.view_class, LogoutSafetyView)

    def test_create_url(self):
        """create ページへのリダイレクトをテスト"""
        url = reverse('users:create')
        self.assertEqual(resolve(url).func.view_class, UserInfoCreateView)

    def test_detail_url(self):
        """detail ページへのリダイレクトをテスト"""
        url = reverse('users:detail', args=[self.object.pk])
        self.assertEqual(resolve(url).func.view_class, UserInfoDetailView)

    def test_update_url(self):
        """update ページへのリダイレクトをテスト"""
        url = reverse('users:update', args=[self.object.pk])
        self.assertEqual(resolve(url).func.view_class, UserInfoUpdateView)

    def test_default_login_url(self):
        """default_login ページへのリダイレクトをテスト"""
        url = reverse('users:default_login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_default_logout_list_url(self):
        """default_logout ページへのリダイレクトをテスト"""
        url = reverse('users:default_logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_guest_login_url(self):
        """guest_login ページへのリダイレクトをテスト"""
        url = reverse('users:guest_login')
        self.assertEqual(resolve(url).func, guest_login)
