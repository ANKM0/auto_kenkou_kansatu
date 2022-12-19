from django import forms
from django.contrib.auth import get_user_model
from .models import UserInfo


User = get_user_model()


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = (
            "user_info_grade_number",
            "user_info_class_number",
            "user_info_student_number",
            "user_info_student_name",
            "user_info_body_temperature",
            "is_run_code",
        )
        field_order = [
            "user_info_grade_number",
            "user_info_class_number",
            "user_info_student_number",
            "user_info_student_name",
            "user_info_body_temperature",
            "is_run_code",
        ]

        labels = {
            'user_info_grade_number': '学年',
            'user_info_class_number': 'クラス番号',
            'user_info_student_number': '出席番号',
            'user_info_student_name': '名前',
            'user_info_body_temperature': '体温',
            'is_run_code': '実行するか',
        }
        help_texts = {
            'user_info_grade_number': '学年を入力',
            'user_info_class_number': 'クラス番号を入力',
            'user_info_student_number': '出席番号を入力',
            'user_info_student_name': '名前を入力',
            'user_info_body_temperature': '体温を入力',
            'is_run_code': '止める時は停止するを選択',
        }
        widgets = {
            "学年": forms.RadioSelect(),
            "実行するか": forms.RadioSelect(),
        }
