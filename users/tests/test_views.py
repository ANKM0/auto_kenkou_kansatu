from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class IndexViewTests(TestCase):
    """IndexViewのテストクラス"""

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)


class HowtoViewTests(TestCase):
    """HowtoViewのテストクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""
        self.password = 'password123'
        self.test_user = get_user_model().objects.create_user(
            username='username',
            email='guestuser@example.com',
            password=self.password
        )
        self.client.login(username=self.test_user.username, email=self.test_user.email, password=self.password)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('users:howto'))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.login(username=self.test_user.username, email=self.test_user.email, password=self.password)


class LogoutSafetyViewTests(TestCase):
    """LogoutSafetyViewのテストクラス"""

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('users:logout_safety'))
        self.assertEqual(response.status_code, 200)


class UserInfoCreateViewTests(TestCase):
    """UserInfoCreateViewのテストクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""
        self.password = 'password123'
        user = get_user_model().objects.create_user(
            username='username',
            email='guestuser@example.com',
            password=self.password
        )
        user.save()
        self.user = user
        self.client.login(username=self.user.username, email=self.user.email, password=self.password)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)

    def test_post_with_data(self):
        """適当なデータで　POST すると、成功してリダイレクトされることを確認"""
        data = {
            # "username": self.user,
            "user_info_grade_number": 3,
            "user_info_class_number": 1,
            "user_info_student_number": 2,
            "user_info_student_name": "gest_user",
            "user_info_body_temperature": 36.5,
            "is_run_code": True,
        }
        response = self.client.post(reverse('users:create'), data=data)
        self.assertEqual(response.status_code, 200)

    def test_post_null(self):
        """空のデータで POST を行うとリダイレクトも無く 200 だけ返されることを確認"""
        data = {}
        response = self.client.post(reverse('users:create'), data=data)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """setUp で追加したデータを消す、掃除用メソッド。"""
        self.client.login(username=self.user.username, email=self.user.email, password=self.password)
