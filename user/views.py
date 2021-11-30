from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin


class LineLogin(View):
    def get(self, request):
        return render(request, 'user/line_login.html')


class IndexView(TemplateView):
    template_name = "user/index.html"


class HowtoView(TemplateView, LoginRequiredMixin):
    template_name = "user/howto.html"


class LogoutView(TemplateView):
    template_name = "user/logout.html"
