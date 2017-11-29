# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView ,UpdateView, FormView
# Create your views here.
from django.http import JsonResponse
from .models import Motherboard, Cpu, Memory, Socket

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'motherboards': Motherboard.objects.all(),
            'cpus': Cpu.objects.all(),
            'memory': Memory.objects.all(),
            'sockets': Socket.objects.all(),
        })
        return context

class AboutView(TemplateView):
    template_name='about.html'

class SearchView(FormView):
    template_name='home.html'
    model=Socket

    def post(self, request, *args,**kwargs):
        search=request.POST.get('socket')
        data = []

        if(search == '*'):
            cpus = Cpu.objects.all()
            for cpu in cpus:
                data.append(cpu.name)

            data.append(";")

            motherboards = Motherboard.objects.all()
            for motherboard in motherboards:
                data.append(motherboard.name)

        else:
            socket = Socket.objects.get(socket=search)

            cpus = socket.cpu.all()
            for cpu in cpus:
                data.append(cpu.name)

            data.append(";")

            motherboards = socket.motherboard.all()
            for motherboard in motherboards:
                data.append(motherboard.name)

        return JsonResponse(data, safe=False)
