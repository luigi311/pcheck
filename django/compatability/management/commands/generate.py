from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from compatability.models import Motherboard, Cpu, Memory
import random, json

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Creating Superuser")
        user=User.objects.create_user('admin', password='password')
        user.is_superuser=True
        user.is_staff=True
        user.save()

        print("Generating Motherboard Data")
        f = open('static/motherboard.json','r')
        data = json.loads(f.read())

        for i in data:
	       d = i.values()
	       m = Motherboard(ratings=d[0], socket=d[1], ram_slots=d[2], price=d[3], name=d[4], max_ram=d[5], form_factor=d[6])
	       m.save()

        f.close()

        print("Generating CPU Data")
        f = open('static/cpu.json','r')
        data = json.loads(f.read())

        for i in data:
            d = i.values()
            c = Cpu(ratings=d[0], price=d[1], name=d[2], socket=d[3])
            c.save()
    
        f.close()

        print("Generating Memory Data")
        f = open('static/memory.json','r')
        data = json.loads(f.read())

        for i in data:
            d = i.values()
            module = d[3].split("-")
            m = Memory(ratings=d[0], name=d[1], cas=d[2], speed=d[3], ram_module=module[0], price=d[4], modules=d[5], price_gb=d[6], ram_type=d[7], size=d[8])
            m.save()
    
        f.close()