from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView



class IndexView(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Comilla Victoria Govt. College'

        return context