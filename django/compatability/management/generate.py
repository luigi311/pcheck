from django.core.management.base import BaseCommand, CommandError

from .models import Motherboard
import random, json

class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open('static/motherboard.json','r')
        data = json.loads(f.read())

        for i in data:
	       d = i.values()
	       m = Motherboard(ratings=d[0], socket=d[1], ram_slots=d[2], price=d[3], name=d[4], max_ram=d[5], form_factor=d[6])
	       m.save()

