import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project18.settings')

import django
django.setup()
import random
from app.models import *
import faker
f=faker.Faker()
L=['Hockey','Circket','VolleyBall','Kabaddi']

def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(L))[0]
    t.save()
    return t

def add_webpage(webpagename,url):
    t=add_topic()
    w=webpage.objects.get_or_create(topic_name=t,name=webpagename,url=url)[0]
    w.save()
    return w

def add_access(webpagename,url,date):
    w=add_webpage(webpagename,url)
    a=Access_Record.objects.get_or_create(name=w,date=date)[0]
    a.save()

def add_data(n):
    for i in range(n):
        fake_name=f.first_name()
        fake_url=f.url()
        fake_date=f.date()
    
        add_access(fake_name,fake_url,fake_date)

if __name__=='__main__':
    print('population is started')
    n=int(input('Enter the no of rows you need:'))
    add_data(n)
    print('population Done Successfully')