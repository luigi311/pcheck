from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from compatability.models import Motherboard, Cpu, Memory, Socket
import random, json


def superuser():
    print("Creating Superuser")
    user=User.objects.create_user('admin', password='password')
    user.is_superuser=True
    user.is_staff=True
    user.save()

def sockets():
    print("Creating Sockets")
    f = open('static/motherboard.json','r')
    c = open('static/cpu.json','r')
    data = json.loads(f.read())
    data2 = json.loads(c.read())
    sockets = []
    for i in data:
        d = i.values()
        sockets.append(d[1])
    for i in data2:
        d = i.values()
        sockets.append(d[3])

    sockets = list(set(sockets))
    for i in sockets:
        s = Socket(socket=i)
        s.save()
    f.close()

def motherboards():
    print("Generating Motherboard Data")
    f = open('static/motherboard.json','r')
    data = json.loads(f.read())

    for i in data:
        d = i.values()
        m = Motherboard(ratings=d[0], socket=Socket.objects.get(socket=d[1]), ram_slots=d[2], price=d[3], name=d[4], max_ram=d[5], form_factor=d[6])
        m.save()

    f.close()

def cpus():
    print("Generating CPU Data")
    f = open('static/cpu.json','r')
    data = json.loads(f.read())

    for i in data:
        d = i.values()
        c = Cpu(ratings=d[0], price=d[1], name=d[2], socket=Socket.objects.get(socket=d[3]))
        c.save()
    
    f.close()

def memory():
    print("Generating Memory Data")
    f = open('static/memory.json','r')
    data = json.loads(f.read())

    for i in data:
        d = i.values()
        module = d[3].split("-")
        m = Memory(ratings=d[0], name=d[1], cas=d[2], speed=d[3], ram_module=module[0], price=d[4], modules=d[5], price_gb=d[6], ram_type=d[7], size=d[8])
        m.save()
    
    f.close()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--superuser',
            action='store_true',
            dest='superuser',
            default=False,
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--sockets',
            action='store_true',
            dest='sockets',
            default=False,
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--motherboards',
            action='store_true',
            dest='motherboards',
            default=False,
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--cpus',
            action='store_true',
            dest='cpus',
            default=False,
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--memory',
            action='store_true',
            dest='memory',
            default=False,
            help='Delete poll instead of closing it',
        )


    def handle(self, *args, **options):
        if options['all']:
            superuser()
            sockets()
            motherboards()
            cpus()
            memory()

        if options['superuser']:
            superuser()

        if options['sockets']:
            sockets()

        if options['motherboards']:
            motherboards()

        if options['cpus']:
            cpus()

        if options['memory']:
            memory()

    