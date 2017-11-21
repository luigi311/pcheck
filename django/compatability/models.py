# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Motherboard(models.Model):
    ratings = models.CharField(max_length=512)
    socket = models.CharField(max_length=512)
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
    socket = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name

class Memory(models.Model):
    ratings = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    cas = models.CharField(max_length=512)
    speed = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    modules = models.CharField(max_length=512)
    price_gb = models.CharField(max_length=512)
    ram_type = models.CharField(max_length=512)
    size = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name


class CpuMotherboard(models.Model):
    cpu = models.ForeignKey(Cpu)
    motherboard = models.ForeignKey(Motherboard)

class MemoryMotherboard(models.Model):
    memory = models.ForeignKey(Memory)
    motherboard = models.ForeignKey(Motherboard)