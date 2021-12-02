from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

# from . import forms
from .forms import UserForm
from .models import Member


APP_LABEL_USER = "users"


class LineLogin(View):
    def get(self, request):
        return render(request, '%s/line_login.html' % APP_LABEL_USER)


class IndexView(TemplateView):
    template_name = '%s/index.html' % APP_LABEL_USER


class HowtoView(TemplateView, LoginRequiredMixin):
    template_name = "%s/howto.html" % APP_LABEL_USER


class LogoutView(TemplateView):
    template_name = "%s/logout.html" % APP_LABEL_USER


def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, '%s/new.html' % APP_LABEL_USER, params)


def list(request):
    data = Member.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, '%s/list.html' % APP_LABEL_USER, params)


# class FormView(TemplateView):

#     # 初期変数定義
#     def __init__(self):
#         self.params = {"Message": "情報を入力してください。",
#                        "form": forms.Contact_Form(),
#                        }

#     # GET時の処理を記載
#     def get(self, request):
#         return render(request, "%s/formpage.html" % APP_LABEL_USER, context=self.params)

#     # POST時の処理を記載
#     def post(self, request):
#         if request.method == "POST":
#             self.params["form"] = forms.Contact_Form(request.POST)

#             # フォーム入力が有効な場合
#             if self.params["form"].is_valid():
#                 self.params["Message"] = "入力情報が送信されました。"

#         return render(request, "%s/formpage.html" % APP_LABEL_USER, context=self.params)
