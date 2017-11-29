# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Socket(models.Model):
    socket=models.CharField(max_length=512)

    def __unicode__(self):
        return self.socket

class Motherboard(models.Model):
    ratings = models.CharField(max_length=512)
    socket = models.ForeignKey(Socket, related_name='motherboard')
    ram_slots = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    max_ram = models.CharField(max_length=512)
    form_factor = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name


class Cpu(models.Model):
    ratings = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    socket = models.ForeignKey(Socket,related_name='cpu')

    def __unicode__(self):
        return self.name


class Memory(models.Model):
    ratings = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    cas = models.CharField(max_length=512)
    speed = models.CharField(max_length=512) 
    ram_module = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    modules = models.CharField(max_length=512)
    price_gb = models.CharField(max_length=512)
    ram_type = models.CharField(max_length=512)
    size = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name


class MemoryMotherboard(models.Model):
    memory = models.ForeignKey(Memory)
    motherboard = models.ForeignKey(Motherboard,related_name="memories")
    