# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


class LoginErrorView(TemplateView):
    template_name = 'error.html'

login_error = LoginErrorView.as_view()
