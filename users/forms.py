from django import forms
from django.contrib.auth import get_user_model
from .models import Member, UserInfo


User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'age')  # 画面に表示させるフィールドを指定
        labels = {
            'name': '名前',
            'age': '年齢'
        }
        help_texts = {
            'name': '名前を入力',
            'age': '年齢を入力'
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("user_info_class_number",
                  "user_info_student_number",
                  "user_info_student_name",
                  "user_info_body_temperature",
                  "is_run_code"
                  )
        field_order = ["user_info_class_number",
                       "user_info_student_number",
                       "user_info_student_name",
                       "user_info_body_temperature",
                       "is_run_code",
                       ]

        labels = {
            'user_info_class_number': 'クラス番号',
            'user_info_student_number': '出席番号',
            'user_info_student_name': '名前',
            'user_info_body_temperature': '体温',
            'is_run_code': '実行するか'
        }
        help_texts = {
            'user_info_class_number': 'クラス番号を入力',
            'user_info_student_number': '出席番号を入力',
            'user_info_student_name': '名前を入力',
            'user_info_body_temperature': '体温を入力',
            'is_run_code': '止める時は停止するを選択'
        }
        widgets = {
            "実行するか": forms.RadioSelect()
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'
