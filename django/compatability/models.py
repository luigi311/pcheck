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