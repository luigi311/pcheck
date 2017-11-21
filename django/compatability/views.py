# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView ,UpdateView
# Create your views here.

from .models import Motherboard, Cpu, Memory

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['motherboards'] = Motherboard.objects.all()
        context['cpus'] = Cpu.objects.all()
        context['memory'] = Memory.objects.all()
        return context

class AboutView(TemplateView):
    template_name='about.html'