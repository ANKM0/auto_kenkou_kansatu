from django.test import TestCase
from users.models import UserInfo
from django.contrib.auth import get_user_model


class UserInfoModelTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username="username", email='guestuser@example.com')
        user.save()
        self.user = user

    def test_is_empty(self):
        saved_objects = UserInfo.objects.all()
        self.assertEqual(saved_objects.count(), 0)

    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""

        object = UserInfo(
            username=self.user,
            user_info_grade_number=3,
            user_info_class_number=1,
            user_info_student_number=2,
            user_info_student_name="test_student_name",
            user_info_body_temperature="test_user_info_body_temperature",
        )
        object.save()
        saved_objects = UserInfo.objects.all()
        self.assertEqual(saved_objects.count(), 1)

    def test_saving_and_retrieving(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""

        object = UserInfo()

        username = self.user
        user_info_grade_number = 3
        user_info_class_number = 1
        user_info_student_number = 2
        user_info_student_name = "test_student_name"
        user_info_body_temperature = "test_user_info_body_temperature"

        object.username = self.user
        object.user_info_grade_number = user_info_grade_number
        object.user_info_class_number = user_info_class_number
        object.user_info_student_number = user_info_student_number
        object.user_info_student_name = user_info_student_name
        object.user_info_body_temperature = user_info_body_temperature
        object.save()

        saved_objects = UserInfo.objects.all()
        actual_object = saved_objects[0]

        self.assertEqual(actual_object.username, username)
        self.assertEqual(actual_object.user_info_grade_number, user_info_grade_number)
        self.assertEqual(actual_object.user_info_class_number, user_info_class_number)
        self.assertEqual(actual_object.user_info_student_number, user_info_student_number)
        self.assertEqual(actual_object.user_info_student_name, user_info_student_name)
        self.assertEqual(actual_object.user_info_body_temperature, user_info_body_temperature)
