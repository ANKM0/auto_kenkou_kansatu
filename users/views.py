from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin


APP_LABEL_1 = "users"


class LineLogin(View):
    def get(self, request):
        return render(request, '%s/line_login.html' % APP_LABEL_1)


class IndexView(TemplateView):
    template_name = '%s/index.html' % APP_LABEL_1


class HowtoView(TemplateView, LoginRequiredMixin):
    template_name = "%s/howto.html" % APP_LABEL_1


class LogoutView(TemplateView):
    template_name = "%s/logout.html" % APP_LABEL_1
