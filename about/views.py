from django.shortcuts import render
from .models import Head, Info
# Create your views here.


def about(request):
    return render(request, "about/about.html", {'hd': Head.objects.get(id=1),
                                                'info': Info.objects.get(id=1),
                                                'title': 'about URI'})
