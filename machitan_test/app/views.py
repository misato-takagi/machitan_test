from django.shortcuts import render
from django.views.generic import TemplateView
#ログインしていない場合はログインページへ進むように設定する
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'app/index.html'

