# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Motherboard, Cpu, Memory, Socket

# Register your models here.
admin.site.register(Motherboard)
admin.site.register(Cpu)
admin.site.register(Memory)
admin.site.register(Socket)