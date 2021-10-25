from django.shortcuts import render
from .models import Team_members, Sections
# Create your views here.


def home(request):
    context = {'teammem': Team_members.objects.all(),
               'sections': Sections.objects.all(),
               'title': 'URI', }
    return render(request, "home/home.html", context)
