from django import forms
from .models import Member, UserInfo


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


class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = {"user_info_class_number",
                  "user_info_student_number",
                  "user_info_student_name",
                  "user_info_body_temperature"}
        labels = {
            'user_info_class_number': 'クラス番号',
            'user_info_student_number': '出席番号',
            'user_info_student_name': '名前',
            'user_info_body_temperature': '体温'
        }
        help_texts = {
            'user_info_class_number': 'クラス番号を入力',
            'user_info_student_number': '出席番号を入力',
            'user_info_student_name': '名前を入力',
            'user_info_body_temperature': '体温を入力'
        }
