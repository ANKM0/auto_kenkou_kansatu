from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "user/index.html"


class HowtoView(TemplateView):
    template_name = "user/howto.html"


class AboutView(TemplateView):
    template_name = "user/about.html"


class InfoView(TemplateView):
    template_name = "user/info.html"


def LineLogin(request):
    """トップ画面"""
    return render(request, 'user/line_login.html')
