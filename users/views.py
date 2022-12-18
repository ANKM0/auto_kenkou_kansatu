from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
from django.shortcuts import render, resolve_url
from django.shortcuts import redirect
from django.contrib.auth import login

from .forms import UserInfoForm
from .models import UserInfo


from.apps import UserConfig
APP_LABEL_USER = UserConfig.name


class LineLogin(View):
    def get(self, request):
        return render(request, '%s/line_login.html' % APP_LABEL_USER)


class IndexView(TemplateView):
    template_name = '%s/index.html' % APP_LABEL_USER


class HowtoView(TemplateView, LoginRequiredMixin):
    template_name = "%s/howto.html" % APP_LABEL_USER


class LogoutSafetyView(TemplateView):
    template_name = "%s/logout_safety.html" % APP_LABEL_USER


def guest_login(request) -> HttpResponse:
    guest_user = get_user_model().objects.get(email='guestuser@example.com')
    login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect("users:index")


class UserInfoCreateView(LoginRequiredMixin, CreateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = "%s/form.html" % APP_LABEL_USER
    success_url = "/"

    def form_valid(self, form):
        userinfo = form.save(commit=False)
        userinfo.username_id = self.request.user.id
        userinfo.save()
        return super().form_valid(form)


class UserInfoDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name = "%s/detail.html" % APP_LABEL_USER

    def get_success_url(self):
        return resolve_url('users:detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        userinfo = form.save(commit=False)
        userinfo.username_id = self.request.user.id
        userinfo.save()
        return super().form_valid(form)


class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = "%s/form.html" % APP_LABEL_USER

    def get_success_url(self):
        return resolve_url('users:detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        userinfo = form.save(commit=False)
        userinfo.username_id = self.request.user.id
        userinfo.save()
        return super().form_valid(form)
