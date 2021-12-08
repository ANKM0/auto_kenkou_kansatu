from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

from .forms import UserInfoForm
from .models import UserInfo
# from django.urls import reverse_lazy

from.apps import UserConfig
APP_LABEL_USER = UserConfig.name


User = get_user_model()


class LineLogin(View):
    def get(self, request):
        return render(request, '%s/line_login.html' % APP_LABEL_USER)


class IndexView(TemplateView):
    template_name = '%s/index.html' % APP_LABEL_USER


class HowtoView(TemplateView, LoginRequiredMixin):
    template_name = "%s/howto.html" % APP_LABEL_USER


class LogoutView(TemplateView):
    template_name = "%s/logout.html" % APP_LABEL_USER


# class OnlyYouMixin(UserPassesTestMixin):
#     raise_exception = True

#     def test_func(self):
#         user = self.request.user
#         return user.pk == self.kwargs['pk'] or user.is_superuser


# class DetailView(OnlyYouMixin, generic.DetailView):
#     model = User
#     template_name = 'user/howto.html'


# class UpdateView(OnlyYouMixin, UpdateView):
#     model = User
#     template_name = "users/update.html"
#     form_class = UserInputForm

#     def get_success_url(self):
#         return resolve_url('users:update', pk=self.kwargs['pk'])


class UserInfoCreateView(CreateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = "%s/list.html" % APP_LABEL_USER
    success_url = "/"  # 成功時にリダイレクトするURL


class UserInfoListView(ListView):
    model = UserInfo
    template_name = "%s/list.html" % APP_LABEL_USER


class UserInfoUpdateView(UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = "%s/form.html" % APP_LABEL_USER
    success_url = "/list"


class UserInfoDeleteView(DeleteView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = "%s/form.html" % APP_LABEL_USER
    success_url = "/list"
