from django.http import HttpResponse
from django.template.loader import get_template
from .forms import CreateSalleForm
from .forms import ReservationForm
from API.models import SalleReunion
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def salles(request):
    return HttpResponse("<h1>page Salles</h1>")
