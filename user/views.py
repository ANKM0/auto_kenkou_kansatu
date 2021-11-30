from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View


class IndexView(TemplateView):
    template_name = "user/index.html"


class HowtoView(TemplateView):
    template_name = "user/howto.html"


class LineLogin(View):
    def get(self, request):
        return render(request, 'user/line_login.html')
