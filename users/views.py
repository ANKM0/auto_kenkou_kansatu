from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserInputForm
from .models import UserInfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# from . import forms

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


# 作成画面
class ItemCreateView(CreateView):
    model = UserInfo
    form_class = UserInputForm
    success_url = reverse_lazy('index')


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    success_url = reverse_lazy('index')


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInputForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = UserInfo
    success_url = reverse_lazy('index')


# def form_view(request):
#     if request.method == 'POST':
#         form = forms.UserInfo(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.username = request.user
#             post.save()
#             return redirect('sns:index')
#     else:
#         form = forms.UserInfo()
#     return render(request, 'users/form_view.html', {'form': form})
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
