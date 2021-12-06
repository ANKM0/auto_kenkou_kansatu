from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm, UserInputForm
from .models import Member, UserInfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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


def input(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('output')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = UserInputForm()
    return render(request, '%s/input.html' % APP_LABEL_USER, params)


def output(request):
    data = UserInfo.objects.all()
    params = {'message': '登録されているデータ', 'data': data}
    return render(request, '%s/output.html' % APP_LABEL_USER, params)


class ItemCreateView(CreateView):
    model = UserInfo
    form_class = UserInputForm


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInputForm
    success_url = reverse_lazy('item')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = UserInfo
    success_url = reverse_lazy('item')

#
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
