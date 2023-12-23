from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render


def show_poster(request):
    return render(request, 'index.html')
