from django.db.models.lookups import StartsWith
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_topic(request):
    topic=Topic.objects.all()
    topic=Topic.objects.all().order_by('topic_name')
    topic=Topic.objects.all().order_by('-topic_name')
    topic=Topic.objects.all().order_by(Length('topic_name'))
    topic=Topic.objects.all().order_by(Length('topic_name').desc())  
    return render(request,'first.html',context={'TP':topic})

def display_webpage(request):
    webpages=webpage.objects.filter(topic_name='Kabaddi')
    webpages=webpage.objects.filter()[0:4:1]
    webpages=webpage.objects.all()
    webpages=webpage.objects.filter().order_by('name')
    webpages=webpage.objects.filter().order_by('-name')
    webpages=webpage.objects.filter().order_by(Length('topic_name').desc())
    webpages=webpage.objects.filter().exclude(topic_name='VolleyBall')
    webpages=webpage.objects.filter(name__in=['Adam','Leah'])
    webpages=webpage.objects.filter(name__contains='D')  
    webpages=webpage.objects.filter(name__startswith='a')
    webpages=webpage.objects.filter(name__endswith='w')
    webpages=webpage.objects.filter(name__regex = r'A[a-zA-Z]{3}')
    webpages=webpage.objects.all()
    webpages=webpage.objects.filter(Q(topic_name='VolleyBall') & Q(url='http://mann-gonzales.org/'))
    webpages=webpage.objects.filter(Q(name='Adam') | Q(url__startswith='https:'))
    webpages=webpage.objects.filter(Q(topic_name='Hockey'))
    webpages=webpage.objects.all()
    return render(request,'second.html',context={'WP':webpages})

def display_Access_Record(request):
    records=Access_Record.objects.all().order_by(Length('name'))
    records=Access_Record.objects.all().order_by('-date')
    records=Access_Record.objects.all()[0:5:1]
    records=Access_Record.objects.filter()[0:5:1]
    records=Access_Record.objects.all()
    records=Access_Record.objects.filter(date='2005-04-08')
    records=Access_Record.objects.filter(date__gt='2005-04-08')
    records=Access_Record.objects.filter(date__gte='2005-04-08')
    records=Access_Record.objects.filter(date__lt='2005-04-08')
    records=Access_Record.objects.filter(date__lte='2005-04-08')
    records=Access_Record.objects.filter(date__month='05')
    records=Access_Record.objects.filter(date__year='2005')
    records=Access_Record.objects.filter(date__day='08')
    return render(request,'third.html',context={'AR':records})

def update_webpage(request):
    webpage.objects.filter(topic_name='VolleyBall').update(name='Ravi')
    webpage.objects.filter(name='Ravi').update(topic_name='Hockey')
    webpage.objects.filter(topic_name='Hockey').update(url='http://www.Hockey.org')

    webpage.objects.update_or_create(name='Leah',defaults={'url':'https://volleyball.org'})
    t=Topic.objects.get_or_create(topic_name='circket')[0]
    t.save()
    webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':t,'name':'Dhoni','url':'https://icc-circket.org'})
    webpages=webpage.objects.all()
    return render(request,'second.html',context={'WP':webpages})

def delete_webpage(request):
    webpage.objects.filter(topic_name='circket').delete()
    webpage.objects.all().delete()
    webpages=webpage.objects.all()
    return render(request,'second.html',context={'WP':webpages})