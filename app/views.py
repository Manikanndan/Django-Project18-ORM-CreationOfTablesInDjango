from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
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
    return render(request,'second.html',context={'WP':webpages})

def display_Access_Record(request):
    records=Access_Record.objects.all()
    records=Access_Record.objects.all().order_by(Length('name'))
    records=Access_Record.objects.all().order_by('-date')
    records=Access_Record.objects.all()[0:5:1]
    records=Access_Record.objects.filter()[0:5:1]
    return render(request,'third.html',context={'AR':records})