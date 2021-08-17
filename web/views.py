from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def page_not_found_view(request):
     return render(request,'web/404.html')

def Home(request):

    eventday1 = Event.objects.filter(Mulai__date= datetime.date(2021, 11, 26))
    eventday2 = Event.objects.filter(Mulai__date= datetime.date(2021, 11, 27))
    pembicara = Pembicara.objects.all().distinct()[:4]

    artikel = Artikel.objects.all().distinct()[:3]

    context = {
        "event": eventday2,
        "eventdate": eventday1,
        "pembicara": pembicara,

        "artikel": artikel,
    }
    return render(request, "web/index.html", context)

def event(request):
    eventday1 = Event.objects.filter(Mulai__date=datetime.date(2021, 11, 24))
    eventday2 = Event.objects.filter(Mulai__date=datetime.date(2021, 11, 25))


    context = {
        "event": eventday2,
        "eventdate": eventday1,

    }
    return render(request, "web/schedule.html", context)

def Speakers(request):
    pembicara = Pembicara.objects.all()

    context = {

        "pembicara": pembicara,

    }
    return render(request, "web/speakers.html", context)

def Teams(request):
    teams = team.objects.all()
    scientific = team.objects.filter(scientific_coord=True)
    context = {

        "teams": teams,
        "scientific": scientific,

    }
    return render(request, "web/teams.html", context)

def Tulisan(request):
    artikel = Artikel.objects.all()

    context = {
        "artikel": artikel,
    }
    return render(request, "web/blog.html", context)

def TulisanDetail(request, artikel_slug):
    artikel = Artikel.objects.get(Slug=artikel_slug)
    

    context = {
        "artikel": artikel,
     
    }
    return render(request, "web/blog-single.html", context)